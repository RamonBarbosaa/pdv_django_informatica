from django.contrib import admin
from .models import Produto, Venda

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade_estoque')
    search_fields = ('nome',)
    list_filter = ('preco',)

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    # O que aparece na lista de vendas
    list_display = ('produto', 'valor_venda', 'data_venda')
    # Adiciona filtros laterais por data
    list_filter = ('data_venda', 'produto')
    # Permite pesquisar pelo nome do produto dentro da venda
    search_fields = ('produto__nome',)