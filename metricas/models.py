from django.db import models


class Metrica(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateTimeField('date published')
    valor = models.IntegerField()