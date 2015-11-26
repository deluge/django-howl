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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('state', models.PositiveSmallIntegerField(default=0, verbose_name='State')),
            ],
            options={
                'verbose_name_plural': 'Alerts',
                'verbose_name': 'Alert',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Observer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('operator', models.CharField(max_length=32, verbose_name='Operator type', choices=[('equal', 'Equals to value'), ('greater', 'Greater than value'), ('lower', 'Lower than value')])),
                ('value', models.PositiveIntegerField(verbose_name='Value')),
                ('waiting_period', models.PositiveIntegerField(help_text='In seconds', verbose_name='Waiting period')),
            ],
            options={
                'verbose_name_plural': 'Observers',
                'verbose_name': 'Observer',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='alert',
            name='observer',
            field=models.ForeignKey(to='howl.Observer', verbose_name='Observer'),
        ),
    ]
