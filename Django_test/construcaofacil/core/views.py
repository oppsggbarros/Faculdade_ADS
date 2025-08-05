from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import F, Sum, Count, Q
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import *
from .forms import *
from decimal import Decimal

@login_required
def index(request):
    # Estatísticas para o dashboard
    total_vendas = Venda.objects.filter(finalizada=True).count()
    total_clientes = Cliente.objects.count()
    total_produtos = Produto.objects.count()
    
    # Produtos com estoque baixo
    produtos_estoque_baixo = Produto.objects.filter(
        estoque_atual__lt=models.F('estoque_minimo')
    ).order_by('estoque_atual')[:5]
    
    # Vendas recentes (calculando o total via annotation)
    vendas_recentes = Venda.objects.filter(finalizada=True).annotate(
        calculo_total=Sum(F('itens__quantidade') * F('itens__preco_unitario')) - F('desconto')
    ).order_by('-data_venda')[:5]
    
    # Total de vendas por dia (últimos 7 dias)
    date_from = timezone.now() - timedelta(days=7)
    vendas_por_dia = Venda.objects.filter(
        finalizada=True,
        data_venda__gte=date_from
    ).extra({
        'day': "date(data_venda)"
    }).values('day').annotate(
        total_vendas=Count('id'),
        valor_total=Sum(F('itens__quantidade') * F('itens__preco_unitario')) - F('desconto')
    ).order_by('day')
    
    context = {
        'total_vendas': total_vendas,
        'total_clientes': total_clientes,
        'total_produtos': total_produtos,
        'produtos_estoque_baixo': produtos_estoque_baixo,
        'vendas_recentes': vendas_recentes,
        'vendas_por_dia': vendas_por_dia,
    }
    
    return render(request, 'core/index.html', context)

@staff_member_required
def lista_produtos(request):
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    
    produtos = Produto.objects.filter(ativo=True)
    
    if query:
        produtos = produtos.filter(
            Q(nome__icontains=query) |
            Q(codigo_barras__icontains=query) |
            Q(descricao__icontains=query)
        )
    
    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)
    
    categorias = Categoria.objects.all()
    
    context = {
        'produtos': produtos,
        'categorias': categorias,
        'query': query,
        'categoria_selecionada': int(categoria_id) if categoria_id else None,
    }
    
    return render(request, 'core/produtos/lista.html', context)

@staff_member_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    
    return render(request, 'core/produtos/form.html', {'form': form, 'titulo': 'Adicionar Produto'})

@staff_member_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'core/produtos/form.html', {'form': form, 'titulo': 'Editar Produto'})

@staff_member_required
def lista_clientes(request):
    query = request.GET.get('q', '')
    
    clientes = Cliente.objects.all()
    
    if query:
        clientes = clientes.filter(
            Q(nome__icontains=query) |
            Q(cpf_cnpj__icontains=query) |
            Q(telefone__icontains=query) |
            Q(email__icontains=query)
        )
    
    context = {
        'clientes': clientes,
        'query': query,
    }
    
    return render(request, 'core/clientes/lista.html', context)

@staff_member_required
def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'core/clientes/form.html', {'form': form, 'titulo': 'Adicionar Cliente'})

@staff_member_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'core/clientes/form.html', {'form': form, 'titulo': 'Editar Cliente'})

@login_required
def nova_venda(request):
    if request.method == 'POST':
        venda_form = VendaForm(request.POST)
        
        if venda_form.is_valid():
            venda = venda_form.save(commit=False)
            
            # Se o usuário for um vendedor, atribui automaticamente
            if hasattr(request.user, 'vendedor'):
                venda.vendedor = request.user.vendedor
            
            venda.save()
            
            # Processar itens da venda
            produtos = request.POST.getlist('produto')
            quantidades = request.POST.getlist('quantidade')
            precos = request.POST.getlist('preco_unitario')
            descontos = request.POST.getlist('desconto_item')
            
            for i in range(len(produtos)):
                if produtos[i] and quantidades[i] and precos[i]:
                    produto = Produto.objects.get(pk=produtos[i])
                    ItemVenda.objects.create(
                        venda=venda,
                        produto=produto,
                        quantidade=quantidades[i],
                        preco_unitario=precos[i],
                        desconto=descontos[i] if descontos[i] else 0
                    )
            
            if 'finalizar' in request.POST:
                venda.finalizada = True
                venda.save()
                return redirect('detalhes_venda', pk=venda.pk)
            
            return redirect('editar_venda', pk=venda.pk)
    else:
        venda_form = VendaForm(initial={
            'vendedor': request.user.vendedor if hasattr(request.user, 'vendedor') else None
        })
    
    produtos = Produto.objects.filter(ativo=True)
    
    return render(request, 'core/vendas/nova.html', {
        'venda_form': venda_form,
        'produtos': produtos,
    })

@login_required
def editar_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    
    if request.method == 'POST':
        venda_form = VendaForm(request.POST, instance=venda)
        
        if venda_form.is_valid():
            venda = venda_form.save()
            
            # Atualizar itens existentes
            item_ids = request.POST.getlist('item_id')
            produtos = request.POST.getlist('produto')
            quantidades = request.POST.getlist('quantidade')
            precos = request.POST.getlist('preco_unitario')
            descontos = request.POST.getlist('desconto_item')
            
            # Primeiro, deletar itens removidos
            existing_ids = [int(id) for id in item_ids if id]
            venda.itens.exclude(id__in=existing_ids).delete()
            
            # Atualizar ou criar itens
            for i in range(len(produtos)):
                if produtos[i] and quantidades[i] and precos[i]:
                    produto = Produto.objects.get(pk=produtos[i])
                    
                    if i < len(item_ids) and item_ids[i]:
                        # Item existente - atualizar
                        item = ItemVenda.objects.get(pk=item_ids[i])
                        item.produto = produto
                        item.quantidade = quantidades[i]
                        item.preco_unitario = precos[i]
                        item.desconto = descontos[i] if descontos[i] else 0
                        item.save()
                    else:
                        # Novo item
                        ItemVenda.objects.create(
                            venda=venda,
                            produto=produto,
                            quantidade=quantidades[i],
                            preco_unitario=precos[i],
                            desconto=descontos[i] if descontos[i] else 0
                        )
            
            if 'finalizar' in request.POST:
                venda.finalizada = True
                venda.save()
                return redirect('detalhes_venda', pk=venda.pk)
            
            return redirect('editar_venda', pk=venda.pk)
    else:
        venda_form = VendaForm(instance=venda)
    
    produtos = Produto.objects.filter(ativo=True)
    itens = venda.itens.all()
    
    return render(request, 'core/vendas/editar.html', {
        'venda': venda,
        'venda_form': venda_form,
        'produtos': produtos,
        'itens': itens,
    })

@login_required
def detalhes_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    return render(request, 'core/vendas/detalhes.html', {'venda': venda})

@login_required
def lista_vendas(request):
    query = request.GET.get('q', '')
    status = request.GET.get('status', 'finalizadas')
    
    vendas = Venda.objects.all()
    
    if query:
        vendas = vendas.filter(
            Q(cliente__nome__icontains=query) |
            Q(vendedor__usuario__username__icontains=query) |
            Q(nfe__icontains=query)
        )
    
    if status == 'finalizadas':
        vendas = vendas.filter(finalizada=True)
    elif status == 'pendentes':
        vendas = vendas.filter(finalizada=False)
    
    vendas = vendas.order_by('-data_venda')
    
    return render(request, 'core/vendas/lista.html', {
        'vendas': vendas,
        'query': query,
        'status': status,
    })

@staff_member_required
def relatorios(request):
    # Vendas por período
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    
    vendas = Venda.objects.filter(finalizada=True)
    
    if date_from:
        vendas = vendas.filter(data_venda__gte=date_from)
    if date_to:
        vendas = vendas.filter(data_venda__lte=date_to)
    
    total_vendas = vendas.count()
    total_valor = vendas.aggregate(total=Sum('total'))['total'] or 0
    
    # Vendas por vendedor
    vendas_por_vendedor = vendas.values(
        'vendedor__usuario__first_name',
        'vendedor__usuario__last_name'
    ).annotate(
        total_vendas=Count('id'),
        total_valor=Sum('total'),
        total_comissao=Sum('comissao_vendedor')
    ).order_by('-total_valor')
    
    # Produtos mais vendidos
    produtos_mais_vendidos = ItemVenda.objects.filter(
        venda__in=vendas
    ).values(
        'produto__nome',
        'produto__categoria__nome'
    ).annotate(
        total_quantidade=Sum('quantidade'),
        total_valor=Sum('total')
    ).order_by('-total_quantidade')[:10]
    
    # Categorias mais vendidas
    categorias_mais_vendidas = ItemVenda.objects.filter(
        venda__in=vendas
    ).values(
        'produto__categoria__nome'
    ).annotate(
        total_quantidade=Sum('quantidade'),
        total_valor=Sum('total')
    ).order_by('-total_valor')
    
    context = {
        'date_from': date_from,
        'date_to': date_to,
        'total_vendas': total_vendas,
        'total_valor': total_valor,
        'vendas_por_vendedor': vendas_por_vendedor,
        'produtos_mais_vendidos': produtos_mais_vendidos,
        'categorias_mais_vendidas': categorias_mais_vendidas,
    }
    
    return render(request, 'core/relatorios/index.html', context)

@login_required
def buscar_produto(request):
    query = request.GET.get('q', '')
    
    produtos = Produto.objects.filter(
        Q(nome__icontains=query) |
        Q(codigo_barras__icontains=query),
        ativo=True
    ).values('id', 'nome', 'preco_venda', 'estoque_atual', 'unidade_medida')[:10]
    
    return JsonResponse(list(produtos), safe=False)

@staff_member_required
def estoque_baixo(request):
    produtos = Produto.objects.filter(
        estoque_atual__lt=models.F('estoque_minimo'),
        ativo=True
    ).order_by('estoque_atual')
    
    return render(request, 'core/relatorios/estoque_baixo.html', {'produtos': produtos})

@staff_member_required
def crediario(request):
    parcelas = ParcelaCrediario.objects.filter(pago=False).order_by('data_vencimento')
    return render(request, 'core/crediario/lista.html', {'parcelas': parcelas})

@staff_member_required
def marcar_parcela_paga(request, pk):
    parcela = get_object_or_404(ParcelaCrediario, pk=pk)
    parcela.pago = True
    parcela.data_pagamento = timezone.now().date()
    parcela.save()
    return redirect('crediario')