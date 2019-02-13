from django import forms

from .models import Itens, Pedidos

class ItensForm(forms.ModelForm):

    class Meta:
        model = Itens
        fields = ('item_quantidade', 'item_preco_escolhido', 'item_produto')

class PedidosForm(forms.ModelForm):

	class Meta:
		model = Pedidos
		fields = ('pedido_cliente',)