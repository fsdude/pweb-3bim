# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-19 05:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provas', '0003_auto_20161019_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questao',
            old_name='prova',
            new_name='disciplina',
        ),
    ]
