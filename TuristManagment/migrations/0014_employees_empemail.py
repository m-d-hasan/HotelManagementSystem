# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuristManagment', '0013_department_employees_mainadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='empEmail',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
