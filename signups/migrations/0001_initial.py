# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
