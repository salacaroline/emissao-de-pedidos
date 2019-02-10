from django.contrib import admin
from pedidos.clientes.models import Clientes

class ClientesAdmin(admin.ModelAdmin):
	model = Clientes
	list_display = ['cliente_id', 'cliente_nome']
	search_fields = ['cliente_nome']
admin.site.register(Clientes, ClientesAdmin)