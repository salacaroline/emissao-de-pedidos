from django.shortcuts import render
from .models import Clientes, Produtos
from .forms import PedidosForm
# Create your views here.
def index(request):
	return render(request, 'emissao/index.html', {})

def cadastro(request):
	clientes = Clientes.objects.all()
	return render(request, 'emissao/cadastrar-pedidos.html', {'clientes':clientes})

def selecionar_produtos(request):
	produtos = Produtos.objects.all()
	return render(request, 'emissao/selecionar-produtos.html', {'produtos':produtos})
def novo_item(request):
	if request.method == "POST":
		form = PedidosForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.save()
		 #return redirect('index')
	else: 
		form = PedidosForm()
	return render(request, 'emissao/novo-item.html', {'form': form})

