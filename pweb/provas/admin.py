#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Esse admin.py é responsável por registrar o conteúdo do models.py na tela de admin.
Provide gerenciamento do banco de dados na tela do admin.
"""
from django.contrib import admin

from .models import Prova, Questao

admin.site.register(Prova)
admin.site.register(Questao)