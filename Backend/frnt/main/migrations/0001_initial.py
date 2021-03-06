# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 17:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FrnTListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('picture', models.ImageField(blank=True, upload_to=main.models.get_image_path)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='FrnTUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, upload_to=main.models.get_image_path)),
                ('biography', models.CharField(blank=True, max_length=500)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('rating_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=15)),
                ('street_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='frntuser',
            name='location',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Location'),
        ),
        migrations.AddField(
            model_name='frntuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='frntlisting',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Location'),
        ),
        migrations.AddField(
            model_name='frntlisting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.FrnTUser', unique=True),
        ),
    ]
