# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-27 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_auto_20170527_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
