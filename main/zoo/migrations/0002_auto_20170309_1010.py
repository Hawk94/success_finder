# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-09 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseanimal',
            name='name',
            field=models.CharField(default='Winter-night', max_length=50),
        ),
        migrations.AlterField(
            model_name='cage',
            name='name',
            field=models.CharField(default='Winter-night', max_length=50),
        ),
        migrations.AlterField(
            model_name='zoo',
            name='name',
            field=models.CharField(default='Winter-night', max_length=50),
        ),
    ]
