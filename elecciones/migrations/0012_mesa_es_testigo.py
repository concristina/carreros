# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0011_circuito_referentes'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='es_testigo',
            field=models.BooleanField(default=False),
        ),
    ]
