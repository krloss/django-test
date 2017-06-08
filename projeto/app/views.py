# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Questao

def index(request):
	return HttpResponse('Olá Mundo!!!')

def lista(request):
	questoes = Questao.objects.order_by('-data')[:5]
	template = loader.get_template('apps/lista.html')
	context = {'questoes':questoes}
	#return HttpResponse(';'.join([q.texto for q in questoes]))
	return HttpResponse(template.render(context,request))

def detalhe(request,questao_id):
	return HttpResponse("Questao %s." % questao_id)

def resultados(request,questao_id):
	response = "Resultados %s."
	return HttpResponse(response % questao_id)

def voto(request,questao_id):
	return HttpResponse("Votou na questao %s." % questao_id)
