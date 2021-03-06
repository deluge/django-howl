# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='observer',
            name='alert_every_time',
            field=models.BooleanField(default=False, verbose_name='Alert every time'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Waiting'), (1, 'Notified')], default=0, verbose_name='State'),
        ),
    ]
