# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone

import datetime
from .models import Questao

# Create your tests here.

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
