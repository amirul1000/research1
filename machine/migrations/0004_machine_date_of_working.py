# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0003_auto_20161109_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='date_of_working',
            field=models.DateField(null=True),
        ),
    ]