
from django.urls import path
from . import views

#Criando rotas html
urlpatterns = [
     path('', views.index, name='index'),
     path('cadastrar-pedido/', views.cadastro, name = 'cadastro'),
     path('cadastrar-pedido/selecionar-produtos/', views.selecionar_produtos, name = 'selecionar_produtos'),
     path('novo-item/', views.novo_item, name='novo_item'),
]