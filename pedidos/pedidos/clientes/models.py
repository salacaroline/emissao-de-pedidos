from django.db import models

class Clientes(models.Model):
	cliente_id = models.AutoField(primary_key = True)
	cliente_nome = models.CharField(max_length = 50)
