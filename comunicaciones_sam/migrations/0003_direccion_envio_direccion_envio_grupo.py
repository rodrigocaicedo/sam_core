# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-14 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('comunicaciones_sam', '0002_auto_20180114_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion_Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('usuario', models.CharField(max_length=300)),
                ('clave', models.CharField(max_length=300)),
                ('host', models.URLField(max_length=500)),
                ('puerto', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion_Envio_Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('grupo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
    ]