# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuristManagment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField(unique=True)),
                ('room_type', models.CharField(max_length=100)),
                ('room_location', models.TextField()),
                ('room_price', models.IntegerField()),
                ('room_size', models.CharField(max_length=50)),
                ('room_view', models.CharField(max_length=50)),
                ('room_bed', models.CharField(max_length=100)),
            ],
        ),
    ]