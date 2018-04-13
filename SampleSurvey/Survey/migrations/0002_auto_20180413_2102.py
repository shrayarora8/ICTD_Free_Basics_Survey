# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='username',
            field=models.CharField(default='noname', max_length=30),
        ),
        migrations.AlterField(
            model_name='answers',
            name='q1',
            field=models.CharField(default='e', max_length=1),
        ),
        migrations.AlterField(
            model_name='answers',
            name='q2',
            field=models.CharField(default='e', max_length=1),
        ),
        migrations.AlterField(
            model_name='answers',
            name='q3',
            field=models.CharField(default='e', max_length=1),
        ),
        migrations.AlterField(
            model_name='answers',
            name='q4',
            field=models.CharField(default='e', max_length=1),
        ),
    ]
