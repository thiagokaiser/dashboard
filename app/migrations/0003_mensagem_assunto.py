# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-22 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mensagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='assunto',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
