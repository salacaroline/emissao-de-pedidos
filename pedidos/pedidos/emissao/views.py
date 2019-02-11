from django.shortcuts import render
from .models import Clientes
# Create your views here.
def index(request):
    return render(request, 'emissao/index.html', {})

def cadastro(request):
	clientes = Clientes.objects.all()
    return render(request, 'emissao/cadastrar-pedidos.html', {})

def selecionar_produtos(request):
    return render(request, 'emissao/selecionar-produtos.html', {})