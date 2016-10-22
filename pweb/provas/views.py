from .forms import *
from .models import *
from django.views import generic
from django.views.generic import *
from django.http import HttpResponseRedirect, HttpResponse

class ResponderProvaView(FormView):
	template_name = 'provas/responder_prova.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		provas = Prova.objects.get(id=self.kwargs['id'])
		questoes = provas.questao_set.all()

		context = {
			'provas': provas,
			'questoes': questoes,
		}

		return context

	def post(self, request, *args, **kwargs):
		form = ProvaResponderForm(request.POST or None)
		if form.is_valid():
			print ("ok")
		

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
					questao_form     = questao_form,
					prova_form       = prova_form
				)
			)