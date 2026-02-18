from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Produto")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Venda")
    quantidade_estoque = models.IntegerField(default=0, verbose_name="Quantidade em Stock")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

# A NOVA CLASSE ENTRA AQUI:
class Venda(models.Model):
    # Relaciona a venda com o produto. Se o produto for apagado, as vendas somem (CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name="Produto Vendido")
    data_venda = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora")
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da Venda")

    def __str__(self):
        return f"{self.produto.nome} - {self.data_venda.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
    