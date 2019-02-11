
from django.urls import path
from . import views

#Criando rotas html
urlpatterns = [
     path('', views.index, name='index'),
]