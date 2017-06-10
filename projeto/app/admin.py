# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Questao,Escolha

# Register your models here.

#class EscolhaInline(admin.StackedInline):
class EscolhaInline(admin.TabularInline):
	model = Escolha
	extra = 3

class QuestaoAdmin(admin.ModelAdmin):
	#fields = ['data','texto']
	fieldsets = [
		(None,{'fields':['texto']}),
		('Informacao',{'fields':['data']}),
	]

	inlines = [EscolhaInline]
	list_display = ('texto','data','recente')
	list_filter = ['data']
	search_fields = ['texto']

#admin.site.register(Questao)
admin.site.register(Questao,QuestaoAdmin)
admin.site.register(Escolha)
