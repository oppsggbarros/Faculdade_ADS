from django.db import models
from django.db.models import Sum, F
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    UNIDADE_CHOICES = [
        ('UN', 'Unidade'),
        ('KG', 'Quilograma'),
        ('MT', 'Metro'),
        ('M2', 'Metro quadrado'),
        ('CX', 'Caixa'),
        ('SC', 'Saco'),
        ('LT', 'Litro'),
    ]
    
    codigo_barras = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    unidade_medida = models.CharField(max_length=2, choices=UNIDADE_CHOICES)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_atual = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    estoque_minimo = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    estoque_maximo = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.get_unidade_medida_display()})"

    @property
    def abaixo_estoque_minimo(self):
        return self.estoque_atual < self.estoque_minimo

    @property
    def acima_estoque_maximo(self):
        return self.estoque_atual > self.estoque_maximo

class Cliente(models.Model):
    TIPO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
    
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default='PF')
    cpf_cnpj = models.CharField(max_length=18, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    comissao_padrao = models.DecimalField(max_digits=5, decimal_places=2, default=5.0)  # porcentagem

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username

class Venda(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('DI', 'Dinheiro'),
        ('CC', 'Cartão de Crédito'),
        ('CD', 'Cartão de Débito'),
        ('PX', 'PIX'),
        ('BO', 'Boleto'),
        ('CR', 'Crediário'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    data_venda = models.DateTimeField(default=timezone.now)
    forma_pagamento = models.CharField(max_length=2, choices=FORMA_PAGAMENTO_CHOICES)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    observacoes = models.TextField(blank=True, null=True)
    nfe = models.CharField(max_length=50, blank=True, null=True)  # Número da NF-e
    finalizada = models.BooleanField(default=False)
    
    def get_total(self):
        return self.itens.aggregate(
            total=Sum(F('quantidade') * F('preco_unitario'))
        )['total'] - self.desconto

    def __str__(self):
        return f"Venda #{self.id} - {self.cliente} ({self.data_venda.strftime('%d/%m/%Y')})"

    @property
    def total_itens(self):
        return sum(item.quantidade for item in self.itens.all())

    @property
    def subtotal(self):
        return sum(item.total for item in self.itens.all())

    @property
    def total(self):
        return self.get_total()

    @property
    def comissao_vendedor(self):
        if self.forma_pagamento in ['CC', 'CD']:
            percentual = 3.0
        else:
            percentual = 5.0
        
        if self.vendedor:
            percentual = self.vendedor.comissao_padrao
            
        return (self.total * percentual) / 100

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(0.001)])
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} (R$ {self.preco_unitario})"

    @property
    def total(self):
        return (self.quantidade * self.preco_unitario) - self.desconto

    def save(self, *args, **kwargs):
        # Atualiza estoque quando o item é salvo
        if self.pk:  # Se já existe no banco (está sendo atualizado)
            old_item = ItemVenda.objects.get(pk=self.pk)
            diferenca = old_item.quantidade - self.quantidade
            self.produto.estoque_atual += diferenca
        else:  # Novo item
            self.produto.estoque_atual -= self.quantidade
        
        self.produto.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Devolve ao estoque quando um item é removido
        self.produto.estoque_atual += self.quantidade
        self.produto.save()
        super().delete(*args, **kwargs)

class ParcelaCrediario(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='parcelas')
    numero = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Parcela {self.numero} de {self.venda}"

    class Meta:
        ordering = ['data_vencimento']