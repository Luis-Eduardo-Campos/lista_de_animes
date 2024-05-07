from django.db import models

# Create your models here.

'''
* id_do_item
* nome
* status_de_finalizado
* resenha
'''
class Registro_de_anime(models.Model):
    nome = models.TextField(max_length=255)
    status_de_finalizado = models.BooleanField(default=False)
    resenha = models.TextField(max_length=5000)
