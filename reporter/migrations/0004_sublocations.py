# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 10:48
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0003_auto_20170505_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sublocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('kensl89g_field', models.FloatField()),
                ('kensl89g_i', models.FloatField()),
                ('subloc', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
