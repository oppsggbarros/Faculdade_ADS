from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'endereco': forms.Textarea(attrs={'rows': 3}),
        }

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'vendedor', 'forma_pagamento', 'desconto', 'observacoes']
        widgets = {
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade', 'preco_unitario', 'desconto']

class ParcelaCrediarioForm(forms.ModelForm):
    class Meta:
        model = ParcelaCrediario
        fields = ['numero', 'valor', 'data_vencimento', 'data_pagamento', 'pago']

class VendedorCreationForm(UserCreationForm):
    telefone = forms.CharField(max_length=20, required=False)
    comissao_padrao = forms.DecimalField(max_digits=5, decimal_places=2, initial=5.0)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Vendedor.objects.create(
                usuario=user,
                telefone=self.cleaned_data['telefone'],
                comissao_padrao=self.cleaned_data['comissao_padrao']
            )
        return user