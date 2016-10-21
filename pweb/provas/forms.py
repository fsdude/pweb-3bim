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