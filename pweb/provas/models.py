from django.db import models
from datetime import date

class Prova(models.Model):
    nivel      = models.IntegerField()
    data       = models.DateField(null = False)
    autor      = models.CharField(max_length=20)
    disciplina = models.CharField(max_length=15)

    def __str__(self):
        return "({0}) - [{1}] - {2} - {3}".format(self.nivel, self.disciplina, self.autor, self.data)

class Questao(models.Model):
	prova               = models.ForeignKey(Prova, on_delete=models.CASCADE)
	descricao           = models.CharField(max_length=200)
	alternativa_correta = models.IntegerField()

	def __str__(self):
		return "[{0}] - {1}".format(self.disciplina, self.alternativa_correta)

class Alternativa(models.Model):
	questao               = models.ForeignKey(Questao, on_delete=models.CASCADE)
	alternativa_descricao = models.CharField(max_length=50)
	alternativa_id 		  = models.IntegerField()

	def __str__(self):
		return "Q: {0} - ID: {1}".format(self.questao, self.alternativa_id)