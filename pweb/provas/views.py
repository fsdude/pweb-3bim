from .forms import *
from .models import *
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
# from django.template import loader
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.views.generic import TemplateView
# from django.views.generic.edit import FormView


# def provas(request):
# 	provas = Prova.objects.all()
# 	questoes = Questao.objects.all()
# 	alternativas = Alternativa.objects.all()

# 	template = loader.get_template('provas/provas.html')
# 	context = {
# 		'provas': provas,
# 		'questoes': questoes,
# 		'alternativas': alternativas,
# 	}

# 	return HttpResponse(template.render(context, request))

class SubmitView(TemplateView):
	template_name = 'provas/submeter.html'

	def get(self, request, *args, **kwargs):
		prova_form       = ProvaForm(self.request.GET or None)
		questao_form     = QuestaoForm(self.request.GET or None)
		alternativa_form = AlternativaForm(self.request.GET or None)

		context = self.get_context_data(**kwargs)
		context['prova_form'] 		= prova_form
		context['questao_form'] 	= questao_form
		context['alternativa_form'] = alternativa_form

		return self.render_to_response(context)

class ProvaFormView(FormView):
	form_class = ProvaForm
	template_name = 'provas/submeter.html'
	success_url = '/'

	def post(self, request, *args, **kwargs):
		prova_form = self.form_class(request.POST)
		questao_form = QuestaoForm()
		alternativa_form = AlternativaForm()

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
					questao_form = questao_form,
					alternativa_form = alternativa_form
				)
			)

class QuestaoFormView(FormView):
	form_class = QuestaoForm
	template_name = 'provas/submeter.html'
	success_url = '/'

	def post(self, request, *args, **kwargs):
		questao_form = self.form_class(request.POST)
		prova_form = ProvaForm()
		alternativa_form = AlternativaForm()

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
					prova_form       = prova_form,
					alternativa_form = alternativa_form
				)
			)

class AlternativaFormView(FormView):
	form_class = AlternativaForm
	template_name = 'provas/submeter.html'
	success_url = '/'

	def post(self, request, *args, **kwargs):
		alternativa_form = self.form_class(request.POST)
		prova_form = ProvaForm()
		questao_form = QuestaoForm()

		if alternativa_form.is_valid():
			alternativa_form.save()
			return self.render_to_response(
				self.get_context_data(
					success = True
				)
			)
		else:
			return self.render_to_response(
				self.get_context_data(
					alternativa_form = alternativa_form,
					prova_form       = prova_form,
					questao_form     = questao_form
				)
			)