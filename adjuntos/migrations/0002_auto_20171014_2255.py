# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-15 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adjuntos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='taken',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='mesa',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachment', to='elecciones.Mesa'),
        ),
    ]
