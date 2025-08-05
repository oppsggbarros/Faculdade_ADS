from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Produtos
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    
    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    
    # Vendas
    path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('vendas/nova/', views.nova_venda, name='nova_venda'),
    path('vendas/editar/<int:pk>/', views.editar_venda, name='editar_venda'),
    path('vendas/detalhes/<int:pk>/', views.detalhes_venda, name='detalhes_venda'),
    
    # Relatórios
    path('relatorios/', views.relatorios, name='relatorios'),
    path('relatorios/estoque-baixo/', views.estoque_baixo, name='estoque_baixo'),
    
    # Crediário
    path('crediario/', views.crediario, name='crediario'),
    path('crediario/marcar-paga/<int:pk>/', views.marcar_parcela_paga, name='marcar_parcela_paga'),
    
    # AJAX
    path('buscar-produto/', views.buscar_produto, name='buscar_produto'),
]