# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0023_mesa_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='taken',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
