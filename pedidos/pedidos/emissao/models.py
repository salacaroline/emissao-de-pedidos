from django.db import models

class Clientes(models.Model):
	cliente_id = models.AutoField(primary_key = True)
	cliente_nome = models.CharField(max_length = 50)

class Produtos(models.Model):
	produto_id = models.AutoField(primary_key = True)
	produto_nome = models.CharField(max_length = 50)
	produto_preco = models.CharField(max_length = 50)
	produto_multiplo = models.IntegerField(null = True, blank = True)

class Itens(models.Model):
	item_id = models.AutoField(primary_key = True)
	item_quantidade = models.IntegerField()
	item_preco_escolhido = models.CharField(max_length = 50, null = True)
	item_produto = models.ForeignKey("Produtos", on_delete = models.CASCADE)

class Pedidos(models.Model):
	pedido_id = models.AutoField(primary_key = True)
	pedido_data = models.DateTimeField(auto_now_add = True)
	pedido_cliente = models.ForeignKey("Clientes", on_delete=models.CASCADE)
	pedido_itens = models.ForeignKey("Itens", on_delete=models.CASCADE, null = True)
