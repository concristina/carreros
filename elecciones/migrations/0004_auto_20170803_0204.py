# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 05:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0003_auto_20170801_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circuito',
            options={'ordering': ('numero',), 'verbose_name': 'Circuito electoral', 'verbose_name_plural': 'Circuitos electorales'},
        ),
        migrations.AlterField(
            model_name='mesa',
            name='lugar_votacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mesas', to='elecciones.LugarVotacion', verbose_name='Lugar de votacion'),
        ),
    ]