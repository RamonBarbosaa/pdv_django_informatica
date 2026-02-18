from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum 
from .models import Produto, Venda 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required # <--- Faltava este import!

@login_required # <--- O CADEADO DA LISTA
def lista_produtos(request):
    termo_pesquisa = request.GET.get('pesquisa', '')
    
    if termo_pesquisa:
        produtos = Produto.objects.filter(nome__icontains=termo_pesquisa)
    else:
        produtos = Produto.objects.all()
    
    ultimas_vendas = Venda.objects.all().order_by('-data_venda')[:10]
    total_faturado = round(Venda.objects.aggregate(Sum('valor_venda'))['valor_venda__sum'] or 0, 2)
    
    return render(request, 'vendas/lista.html', {
        'produtos': produtos,
        'total_faturado': total_faturado,
        'ultimas_vendas': ultimas_vendas,
        'termo_pesquisa': termo_pesquisa
    })

@login_required # <--- O CADEADO DA VENDA
def realizar_venda(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if produto.quantidade_estoque > 0:
        produto.quantidade_estoque -= 1
        produto.save()
        
        Venda.objects.create(
            produto=produto,
            valor_venda=produto.preco
        )
        messages.success(request, f"Venda de {produto.nome} realizada!")
    else:
        messages.error(request, f"Erro: {produto.nome} está sem estoque!")
    
    return redirect('lista_produtos')