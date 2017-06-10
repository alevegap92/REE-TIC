# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-10 03:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='proyecto_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, upload_to='logos')),
                ('descripcion_general', models.TextField(blank=True, max_length=200)),
                ('descripcion_detallada', models.TextField(blank=True, max_length=1500)),
                ('definicion_problema', models.TextField(blank=True, max_length=1500)),
                ('definicion_solucion', models.TextField(blank=True, max_length=1500)),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(auto_now=True)),
                ('donate', models.IntegerField(blank=True)),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='proyecto_picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
