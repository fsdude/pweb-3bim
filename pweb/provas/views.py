from .forms import *
from .models import *
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse


def provas(request):
	provas = Prova.objects.all()
	questoes = Questao.objects.all()
	alternativas = Alternativa.objects.all()

	template = loader.get_template('provas/provas.html')
	context = {
		'provas': provas,
		'questoes': questoes,
		'alternativas': alternativas,
	}

	return HttpResponse(template.render(context, request))

def submeter(request):
	template = loader.get_template('provas/submeter.html')

	form1 = ProvaForm(prefix="form1")
	form2 = QuestaoForm(prefix="form2")
	form3 = AlternativaForm(prefix="form3")

	if request.POST:
		form1 = ProvaForm(request.POST, prefix="form1")
		form2 = QuestaoForm(request.POST, prefix="form2")
		form3 = AlternativaForm(request.POST, prefix="form3")
		
		if form1.is_valid() and form2.is_valid() and form3.is_valid():
			nova_prova = Prova.objects.create(nivel      = form1.cleaned_data['nivel'],
											  data       = form1.cleaned_data['data'],
											  autor 	 = form1.cleaned_data['autor'],
											  disciplina = form1.cleaned_data['disciplina'])

			print ("111111111")
			
			nova_questao = Prova.objects.create(descricao           = form2.cleaned_data['descricao'],
											    alternativa_correta = form2.cleaned_data['alternativa_correta'])

			print ("222222222")
											  
			nova_alternativa = Prova.objects.create(alternativa_descricao = form3.cleaned_data['alternativa_descricao'],
											  		alternativa_id        = form3.cleaned_data['alternativa_id'])
											  
			nova_prova.save()
			nova_questao.save()
			nova_alternativa.save()

			return HttpResponse(template.render({}, request))

	#Caso não seja, criar formulário vazio
	else:
		form1 = ProvaForm(prefix="form1")
		form2 = QuestaoForm(prefix="form2")
		form3 = AlternativaForm(prefix="form3")

		return HttpResponse(template.render({'form1': form1, 'form2': form2, 'form3': form3}, request))