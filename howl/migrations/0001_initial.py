# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('state', models.PositiveSmallIntegerField(default=0, verbose_name='State')),
            ],
            options={
                'verbose_name': 'Alert',
                'verbose_name_plural': 'Alerts',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Observer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('comparator', models.CharField(max_length=32, verbose_name='Comparator type', choices=[('equal', 'Comparator that equals to value')])),
                ('value', models.PositiveIntegerField(verbose_name='Value')),
                ('tolerance', models.PositiveSmallIntegerField(help_text='In percent', default=0, verbose_name='Tolerance')),
                ('waiting_period', models.PositiveIntegerField(help_text='In seconds', verbose_name='Waiting period')),
            ],
            options={
                'verbose_name': 'Observer',
                'verbose_name_plural': 'Observers',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='alert',
            name='observer',
            field=models.ForeignKey(to='howl.Observer', verbose_name='Observer'),
        ),
    ]
