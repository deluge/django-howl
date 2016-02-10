# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howl', '0004_auto_20160210_0811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='observer',
        ),
        migrations.AddField(
            model_name='alert',
            name='identifier',
            field=models.CharField(default='', verbose_name='Identifier', max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alert',
            name='value',
            field=models.CharField(verbose_name='Value', blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='observer',
            name='value',
            field=models.IntegerField(verbose_name='Value'),
        ),
    ]
