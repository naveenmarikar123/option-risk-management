# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxpain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionchain',
            name='stock_symbol',
            field=models.CharField(default='HINDALCO', max_length=100),
            preserve_default=False,
        ),
    ]