# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 01:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('accounts', '0002_organization_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='member',
            name='logins',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='BaseUser',
        ),
    ]
