# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-20 00:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provas', '0005_auto_20161019_0302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alternativa',
            name='questao',
        ),
        migrations.DeleteModel(
            name='Alternativa',
        ),
    ]
