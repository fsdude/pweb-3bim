#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Esse views.py é responsável pelo processamento dos dados.
É aqui é decidido os quais valores serão renderizados
no template.

'ResponderProvaFormView':
	retorna a quantidade de acertos da prova resolvida

'VisualizarProvaView':
	retorna a prova selecionada pelo usuário para
	ser visualizada

'SubmitView':
	manda para o template quais os campos dos forms devem
	ser preenchidos


'ProvaFormView' e 'QuestaoFormView':
	salvam os dados inseridos nos forms no banco de dados
"""
from .forms import ProvaForm, QuestaoForm
from .models import Prova, Questao
from django.views.generic import FormView, TemplateView

class ResponderProvaFormView(TemplateView):
	template_name = 'provas/responder_prova.html'

	def get_context_data(self, **kwargs):
		provas = Prova.objects.get(id=self.kwargs['id'])
		questoes = provas.questao_set.all()

		acertos = self.acertos
		total   = self.questoes.count()
		success = self.success
		context = {
			'provas': provas,
			'questoes': questoes,
			'acertos': acertos,
			'total': total,
			'success': success,
		}

		return context

	def get(self, request, *args, **kwargs):
		provas = Prova.objects.get(id=self.kwargs['id'])
		self.questoes = provas.questao_set.all()
		self.respostas_list   = []
		self.questao_ids      = []
		self.questao_ids_fake = []
		self.alternativa_list = []
		self.acertos          = 0
		self.success          = False

		for resposta in range(0, (self.questoes.count())):
			self.questao_ids_fake.append(self.questoes.values_list('id')[resposta])
			self.questao_ids.append(''.join(map(str, self.questao_ids_fake[resposta])))

		for resposta in range(0, self.questoes.count()):
			x = self.questao_ids[resposta]
			self.respostas_list.append(request.GET.get(str(x)))

		self.questao_list = Questao.objects.filter(id__in=self.questao_ids)	

		for x in range(0, (self.questoes.count())):
			alt_list = [
				(self.questao_list[x].alternativa_a),
				(self.questao_list[x].alternativa_b),
				(self.questao_list[x].alternativa_c),
				(self.questao_list[x].alternativa_d),
				(self.questao_list[x].alternativa_e)
			]
			self.alternativa_list.append(alt_list)


		for resposta in range(1, self.questoes.count()+1):
			if self.respostas_list[resposta-1] == self.alternativa_list[resposta-1][self.questao_list[resposta-1].alternativa_correta-1]:
				self.acertos += 1
				self.success = True
			elif self.respostas_list[resposta-1] is None:
				self.success = False
			else:
				self.success = True

		return self.render_to_response(
			self.get_context_data(
				success = True
			)
		)

class VisualizarProvaView(TemplateView):
	template_name = 'provas/visualizar_prova.html'

	def get_context_data(self, **kwargs):
		provas = Prova.objects.get(id=self.kwargs['id'])
		questoes = provas.questao_set.all()

		context = {
			'provas': provas,
			'questoes': questoes,
		}

		return context

class SubmitView(TemplateView):
	template_name = 'provas/submeter.html'

	def get(self, request, *args, **kwargs):
		prova_form        = ProvaForm(self.request.GET or None)
		questao_form      = QuestaoForm(self.request.GET or None)

		context = self.get_context_data(**kwargs)
		context['prova_form'] 		= prova_form
		context['questao_form'] 	= questao_form

		return self.render_to_response(context)

	def get_context_data(self, **kwargs):
		provas = Prova.objects.all()
		questoes = Questao.objects.all()
		
		context = {
			'provas': provas,
			'questoes': questoes,
		}

		return context

class ProvaFormView(FormView):
	form_class = ProvaForm
	template_name = 'provas/submeter.html'
	success_url = '/'

	def post(self, request, *args, **kwargs):
		prova_form = self.form_class(request.POST)
		questao_form = QuestaoForm()

		if prova_form.is_valid():
			prova_form.save()
			return self.render_to_response(
				self.get_context_data(
					success = True
				)
			)
		else:
			return self.render_to_response(
				self.get_context_data(
					prova_form   = prova_form,
					questao_form = questao_form
				)
			)

class QuestaoFormView(FormView):
	form_class = QuestaoForm
	template_name = 'provas/submeter.html'
	success_url = '/'

	def post(self, request, *args, **kwargs):
		questao_form = self.form_class(request.POST)
		prova_form = ProvaForm()

		if questao_form.is_valid():
			questao_form.save()
			return self.render_to_response(
				self.get_context_data(
					success = True
				)
			)
		else:
			return self.render_to_response(
				self.get_context_data(
					questao_form = questao_form,
					prova_form   = prova_form
				)
			)