# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-28 13:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_mensagem_lida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensagem',
            name='user',
        ),
        migrations.AlterField(
            model_name='mensagem',
            name='destinatario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
