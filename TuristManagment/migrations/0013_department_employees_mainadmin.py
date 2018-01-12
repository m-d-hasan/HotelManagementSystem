# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TuristManagment', '0012_hoteladmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptID', models.CharField(max_length=30)),
                ('deptName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empID', models.IntegerField()),
                ('empName', models.CharField(max_length=50)),
                ('empAddress', models.CharField(max_length=100)),
                ('empCity', models.CharField(max_length=30)),
                ('empCounty', models.CharField(max_length=30)),
                ('deptid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TuristManagment.Employees')),
            ],
        ),
        migrations.CreateModel(
            name='mainAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminName', models.CharField(max_length=50)),
                ('adminPassword', models.CharField(max_length=32)),
            ],
        ),
    ]