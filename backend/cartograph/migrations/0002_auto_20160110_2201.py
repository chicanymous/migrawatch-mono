# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartograph', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raid',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='raid',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
