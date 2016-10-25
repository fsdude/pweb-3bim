#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
models.py é responsável por criar/atualizar/deletar o banco de dados.
Ele converte esse código em python para a linguagem usada do bd
e consegue criar as TABLES e COLUMNs.

'Prova' e 'Questao' são as tabelas do banco de dados.
	E 'Questao' aponta para Prova, então uma 'Prova' pode ter
	muitas 'Questao'.
"""
from django.db import models

class Prova(models.Model):
	NIVEL_PROVA = ((1, 'Fácil'), (2, 'Normal'), (3, 'Difícil'))

	nivel      = models.IntegerField(default=2, choices=NIVEL_PROVA)
	data       = models.DateField(null=False)
	autor      = models.CharField(max_length=20)
	disciplina = models.CharField(max_length=15)

	def __str__(self):
		return "({0}) - [{1}] - {2} - {3}".format(self.nivel, self.disciplina, self.autor, self.data)

class Questao(models.Model):
	ALTERNATIVA_CERTA = ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'))

	prova                = models.ForeignKey(Prova, on_delete=models.CASCADE)
	enunciado            = models.CharField(null=True, max_length=200)
	alternativa_a        = models.CharField(null=True, max_length=50)
	alternativa_b        = models.CharField(null=True, max_length=50)
	alternativa_c        = models.CharField(null=True, max_length=50)
	alternativa_d        = models.CharField(null=True, max_length=50)
	alternativa_e 		 = models.CharField(null=True, max_length=50)
	alternativa_correta  = models.IntegerField(choices=ALTERNATIVA_CERTA)

	def __str__(self):
		return "{0} | {1} |".format(self.enunciado, self.alternativa_correta)