from django.shortcuts import render
from .models import Clientes, Produtos, Pedidos, Itens
from .forms import ItensForm
# Create your views here.
def index(request):
	return render(request, 'emissao/index.html', {})

def clientes(request):
	clientes = Clientes.objects.all()
	return render(request, 'emissao/clientes.html', {'clientes':clientes})

def cadastro(request):
	clientes = Clientes.objects.all()
	return render(request, 'emissao/cadastrar-pedidos.html', {'clientes':clientes})

def selecionar_produtos(request):
	produtos = Produtos.objects.all()
	return render(request, 'emissao/selecionar-produtos.html', {'produtos':produtos})

def novo_item(request, pk):
	if request.method == "POST":
		form = ItensForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.save()
		cliente = Clientes.objects.get(cliente_id=pk)
		item_obj = Itens.objects.get(item_id = item.item_id)
		pedido = Pedidos.objects.create(pedido_cliente = cliente)
		pedido.pedido_itens.add(item_obj)


	else: 
		form = ItensForm()
	return render(request, 'emissao/novo-item.html', {'form': form})

