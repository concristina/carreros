# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-16 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adjuntos', '0003_auto_20171016_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='problema',
            field=models.CharField(blank=True, choices=[('no es una foto válida', 'no es una foto válida'), ('no se entiende', 'no se entiende'), ('foto rotada', 'foto rotada')], max_length=100, null=True),
        ),
    ]
