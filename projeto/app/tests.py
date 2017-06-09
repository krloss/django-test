# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

import datetime
from .models import Questao

# Create your tests here.

def criar_questao(texto,dias):
	time = timezone.now() + datetime.timedelta(days=dias)
	return Questao.objects.create(texto=texto, data=time)

class QuestaoDetalheViewTestes(TestCase):
	def teste_futura_questao(self):
		fq = criar_questao(texto='Futuro', dias=5)
		url = reverse('detalhe',args=(fq.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code,404)

	def teste_antiga_questao(self):
		aq = criar_questao(texto='Antigo', dias=-5)
		url = reverse('detalhe',args=(aq.id,))
		response = self.client.get(url)
		self.assertContains(response,aq.texto)

class QuestaoViewTestes(TestCase):
	def teste_sem_questao(self):
		response = self.client.get(reverse('questoes'))

		self.assertEqual(response.status_code,200)
		self.assertContains(response,"Nenhuma Questao")
		self.assertQuerysetEqual(response.context['questoes'],[])

	def teste_antiga_questao(self):
		criar_questao(texto='Antigo', dias=-30)
		response = self.client.get(reverse('questoes'))
		self.assertQuerysetEqual(response.context['questoes'],['<Questao: Antigo>'])

	def teste_futura_questao(self):
		criar_questao(texto='Futuro', dias=30)
		response = self.client.get(reverse('questoes'))
		self.assertContains(response,'Nenhuma Questao')
		self.assertQuerysetEqual(response.context['questoes'],[])

	def teste_futura_antiga_questao(self):
		criar_questao(texto='Antigo', dias=-30)
		criar_questao(texto='Futuro', dias=30)
		response = self.client.get(reverse('questoes'))
		self.assertQuerysetEqual(response.context['questoes'],['<Questao: Antigo>'])

	def teste_duas_antigas_questoes(self):
		criar_questao(texto='Antigo 1', dias=-30)
		criar_questao(texto='Antigo 2', dias=-5)
		response = self.client.get(reverse('questoes'))
		self.assertQuerysetEqual(response.context['questoes'],
			['<Questao: Antigo 2>','<Questao: Antigo 1>'])

class QuestaoModelTests(TestCase):
	def teste_recente_futuro(self):
		"""
			was_published_recently() returns False for questions
			whose pub_date is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		futuro = Questao(data=time)
		self.assertIs(futuro.recente(),False)

	def teste_recente_antigo(self):
		time = timezone.now() - datetime.timedelta(days=1)
		futuro = Questao(data=time)
		self.assertIs(futuro.recente(),False)

	def teste_recente_recente(self):
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		futuro = Questao(data=time)
		self.assertIs(futuro.recente(),True)
