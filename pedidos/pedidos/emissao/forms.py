from django import forms

from .models import Itens

class PedidosForm(forms.ModelForm):

    class Meta:
        model = Itens
        fields = ('item_quantidade', 'item_preco_escolhido', 'item_produto')