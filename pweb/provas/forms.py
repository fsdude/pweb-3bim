from django.forms import ModelForm
from provas.models import Prova, Questao, Alternativa

class ProvaForm(ModelForm):
	class Meta:
		model = Prova
		fields = ['nivel', 'data', 'autor', 'disciplina']

class QuestaoForm(ModelForm):
	class Meta:
		model = Questao
		fields = ['prova', 'descricao', 'alternativa_correta']

class AlternativaForm(ModelForm):
	class Meta:
		model = Alternativa
		fields = ['questao', 'alternativa_descricao', 'alternativa_id']