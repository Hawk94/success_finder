# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=1000)),
                ('priority', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], max_length=1)),
                ('category', models.CharField(max_length=50)),
                ('issue_type', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], max_length=1)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.Contract')),
                ('sf_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.Contact')),
            ],
        ),
    ]
