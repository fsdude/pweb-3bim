#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Esse forms.py ajuda a criar o formulário. 
Ele auxilia na validação e nesse caso evitando redundância

'ProvaForm' e 'QuestaoForm' são formulários baseados no banco de dados já criados. 
Portanto eles têm os mesmos campos do bd.
"""
from django.forms import ModelForm
from provas.models import Prova, Questao

class ProvaForm(ModelForm):
	class Meta:
		model = Prova
		fields = ['nivel', 'data', 'autor', 'disciplina']

class QuestaoForm(ModelForm):
	class Meta:
		model = Questao
		fields = ['prova', 'enunciado', 'alternativa_a', 'alternativa_b',
		 'alternativa_c', 'alternativa_d', 'alternativa_e' ,'alternativa_correta']