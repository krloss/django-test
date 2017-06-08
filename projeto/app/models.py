# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Questao(models.Model):
	texto = models.CharField(max_length=200)
	data = models.DateTimeField('date published')

class Escolha(models.Model):
	questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
	texto = models.CharField(max_length=100)
	voto = models.IntegerField(default=0)
