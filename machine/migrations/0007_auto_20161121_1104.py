# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161029223924 on 2016-11-21 05:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0006_auto_20161121_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_files', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.RemoveField(
            model_name='machine',
            name='pdf_files',
        ),
        migrations.AddField(
            model_name='uploadfiles',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.Machine'),
        ),
    ]