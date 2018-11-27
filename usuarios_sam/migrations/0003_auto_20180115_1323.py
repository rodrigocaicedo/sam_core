# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-15 18:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_sam', '0002_auto_20180114_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='id_students',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Estudiante', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
