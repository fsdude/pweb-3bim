# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-19 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='alternativa_correta',
            field=models.IntegerField(),
        ),
    ]