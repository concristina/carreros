# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 04:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiscales', '0007_auto_20170803_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiscal',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fiscal', to=settings.AUTH_USER_MODEL),
        ),
    ]