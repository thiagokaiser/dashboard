# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180228_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='foto_perfil',
            field=models.FileField(blank=True, null=True, upload_to='perfil/'),
        ),
    ]
