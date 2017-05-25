# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-24 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0003_auto_20170519_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='publicacion',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
