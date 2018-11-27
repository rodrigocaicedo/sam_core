# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-26 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='/messages/attachments')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_attachment', models.FileField(blank=True, null=True, upload_to=b'')),
                ('original_filename', models.CharField(default=None, max_length=250)),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
        ),
        migrations.CreateModel(
            name='Comunicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MailerMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('to_address', models.TextField(verbose_name='To')),
                ('bcc_address', models.TextField(blank=True, verbose_name='BCC')),
                ('from_address', models.EmailField(max_length=250, verbose_name='From')),
                ('reply_to', models.TextField(blank=True, max_length=250, null=True, verbose_name='Reply to')),
                ('app', models.CharField(blank=True, max_length=250, verbose_name='App')),
                ('sent', models.BooleanField(default=False, editable=False, verbose_name='Sent')),
                ('last_attempt', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Last attempt')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comunicaciones_sam.Comunicacion')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.AddField(
            model_name='attachment',
            name='email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comunicaciones_sam.MailerMessage'),
        ),
        migrations.AddField(
            model_name='adjunto',
            name='attached_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comunicaciones_sam.Comunicacion'),
        ),
    ]