from django.contrib import admin
from .models import *

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco_venda', 'estoque_atual', 'unidade_medida', 'ativo')
    list_filter = ('categoria', 'ativo')
    search_fields = ('nome', 'codigo_barras', 'descricao')
    list_editable = ('preco_venda', 'ativo')
    readonly_fields = ('estoque_atual',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'cpf_cnpj', 'telefone', 'email')
    search_fields = ('nome', 'cpf_cnpj', 'telefone', 'email')
    list_filter = ('tipo',)

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefone', 'comissao_padrao')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name', 'telefone')

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1
    readonly_fields = ('total',)

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'vendedor', 'data_venda', 'forma_pagamento', 'total', 'finalizada')
    list_filter = ('data_venda', 'forma_pagamento', 'finalizada', 'vendedor')
    search_fields = ('cliente__nome', 'vendedor__usuario__username', 'nfe')
    inlines = [ItemVendaInline]
    readonly_fields = ('subtotal', 'total', 'comissao_vendedor')

    def subtotal(self, obj):
        return obj.subtotal
    subtotal.short_description = 'Subtotal'

    def total(self, obj):
        return obj.total
    total.short_description = 'Total'

    def comissao_vendedor(self, obj):
        return obj.comissao_vendedor
    comissao_vendedor.short_description = 'Comissão'

@admin.register(ParcelaCrediario)
class ParcelaCrediarioAdmin(admin.ModelAdmin):
    list_display = ('venda', 'numero', 'valor', 'data_vencimento', 'pago')
    list_filter = ('pago', 'data_vencimento')
    search_fields = ('venda__cliente__nome',)
    list_editable = ('pago',)