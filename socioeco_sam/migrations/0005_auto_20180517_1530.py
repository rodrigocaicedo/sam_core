# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-17 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socioeco_sam', '0004_evaluacion_socioeco_familia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='gastos_alimentacion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='gastos',
            name='gastos_educacion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='gastos',
            name='gastos_salud',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='gastos',
            name='gastos_transporte',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='gastos',
            name='gastos_vestimenta',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='gastos',
            name='gastos_vivienda',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='arriendos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='dependencias',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='inversiones',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='negocios',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
