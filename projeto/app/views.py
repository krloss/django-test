# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Questao,Escolha

# Create your views here.
def index(request):
	return HttpResponse('<a href="/app/list">Olá Mundo!!!</a>')

def lista(request):
	questoes = Questao.objects.order_by('-data')[:5]
	template = loader.get_template('apps/lista.html')
	context = {'questoes':questoes}
	#return HttpResponse(';'.join([q.texto for q in questoes]))
	return HttpResponse(template.render(context,request))

class QuestoesView(generic.ListView):
	template_name = 'apps/lista.html'
	context_object_name = 'questoes'

	def get_queryset(self):
		return Questao.objects.order_by('-data')[:5]

def detalhe(request,questao_id):
	#try:
	#	q = Questao.objects.get(pk=questao_id)
	#except Questao.DoesNotExist:
	#	raise Http404('Questao Inexistente')
	q = get_object_or_404(Questao, pk=questao_id)
	#return HttpResponse("Questao %s." % questao_id)
	return render(request,'apps/detail.html',{'questao':q})

class DetailView(generic.DetailView):
	model = Questao
	template_name = 'apps/detail.html'

def resultados(request,questao_id):
	q = get_object_or_404(Questao, pk=questao_id)
	return render(request,'apps/results.html',{'questao':q})

def voto(request,questao_id):
	q = get_object_or_404(Questao, pk=questao_id)

	try:
		escolha = q.escolha_set.get(pk=request.POST['escolha'])
	except (KeyError,Escolha.DoesNotExist):
		return render(request,'apps/detail.html',{'questao':q, 'error_message':'Sem Escolha.'})
	else:
		escolha.voto += 1
		escolha.save()
		return HttpResponseRedirect(reverse('resultados', args=(q.id,)))

	return HttpResponse("Votou na questao %s." % questao_id)
