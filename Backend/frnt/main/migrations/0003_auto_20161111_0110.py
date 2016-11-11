# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 01:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161109_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
