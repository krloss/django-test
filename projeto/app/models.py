# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Questao(models.Model):
	texto = models.CharField(max_length=200)
	data = models.DateTimeField('publicacao')

	def __str__(self):
		return self.texto

	def recente(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.data <= now

	recente.admin_order_field = 'data'
	recente.boolean = True
	recente.short_description = 'Novo?'

class Escolha(models.Model):
	questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
	texto = models.CharField(max_length=100)
	voto = models.IntegerField(default=0)

	def __str__(self):
		return self.texto
