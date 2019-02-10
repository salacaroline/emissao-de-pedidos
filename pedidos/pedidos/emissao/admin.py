from django.contrib import admin

from pedidos.emissao.models import Clientes, Produtos, Pedidos

class ClientesAdmin(admin.ModelAdmin):
	model = Clientes
	list_display = ['cliente_id', 'cliente_nome']
	search_fields = ['cliente_nome']
admin.site.register(Clientes, ClientesAdmin)

class ProdutosAdmin(admin.ModelAdmin):
	model = Produtos
	list_display = ['produto_id', 'produto_nome', 'produto_preco', 'produto_multiplo']
	search_fields = ['produto_nome']
admin.site.register(Produtos, ProdutosAdmin)

class PedidosAdmin(admin.ModelAdmin):
	model = Pedidos
	list_display = ['pedido_id', 'pedido_data', 'pedido_cliente']
	search_fields = ['pedido_data', 'pedido_cliente', 'pedido_produto']
admin.site.register(Pedidos, PedidosAdmin)