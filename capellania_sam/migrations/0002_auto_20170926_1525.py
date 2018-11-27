# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-26 20:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('capellania_sam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='informeseguimiento',
            name='capellan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Capellan'),
        ),
        migrations.AddField(
            model_name='informeseguimiento',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Estudiante'),
        ),
        migrations.AddField(
            model_name='informeseguimiento',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Profesor'),
        ),
        migrations.AddField(
            model_name='informeremision',
            name='capellan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Capellan'),
        ),
        migrations.AddField(
            model_name='informeremision',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Estudiante'),
        ),
        migrations.AddField(
            model_name='informeremision',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Profesor'),
        ),
        migrations.AddField(
            model_name='informenovedades',
            name='capellan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Capellan'),
        ),
        migrations.AddField(
            model_name='informenovedades',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Estudiante'),
        ),
        migrations.AddField(
            model_name='informenovedades',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Profesor'),
        ),
        migrations.AddField(
            model_name='informegeneral',
            name='capellan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Capellan'),
        ),
        migrations.AddField(
            model_name='informegeneral',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Estudiante'),
        ),
        migrations.AddField(
            model_name='informegeneral',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capellania_sam.Profesor'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='controldeformulario',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='capellan',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
