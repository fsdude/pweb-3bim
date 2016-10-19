from django import forms
from .models import Prova, Questao, Alternativa
from datetime import date

class DateWidget(forms.DateInput):
	input_type = "date"

class ProvaForm(forms.Form):
    nivel      = forms.IntegerField(label='nivel')
    data       = forms.DateField(label='data', widget=DateWidget())
    autor      = forms.CharField(label='autor', max_length=20)
    disciplina = forms.CharField(label='disciplina', max_length=15)

class QuestaoForm(forms.Form):
	descricao           = forms.CharField(max_length=200)
	alternativa_correta = forms.IntegerField()

class AlternativaForm(forms.Form):
	alternativa_descricao = forms.CharField(max_length=50)
	alternativa_id 		  = forms.IntegerField()
