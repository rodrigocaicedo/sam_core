# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-15 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_sam', '0004_auto_20180114_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccion',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]