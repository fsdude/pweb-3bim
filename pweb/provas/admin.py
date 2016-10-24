#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Prova, Questao

admin.site.register(Prova)
admin.site.register(Questao)