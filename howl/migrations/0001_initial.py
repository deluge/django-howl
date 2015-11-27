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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('state', models.PositiveSmallIntegerField(default=0, verbose_name='State')),
            ],
            options={
                'verbose_name_plural': 'Alerts',
                'ordering': ('-timestamp',),
                'verbose_name': 'Alert',
            },
        ),
        migrations.CreateModel(
            name='Observer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('operator', models.CharField(choices=[('EqualOperator', 'Equals to value'), ('GreaterThanOperator', 'Greater than value'), ('LowerThanOperator', 'Lower than value')], verbose_name='Operator type', max_length=32)),
                ('value', models.PositiveIntegerField(verbose_name='Value')),
                ('waiting_period', models.PositiveIntegerField(help_text='In seconds', verbose_name='Waiting period')),
            ],
            options={
                'verbose_name_plural': 'Observers',
                'ordering': ('name',),
                'verbose_name': 'Observer',
            },
        ),
        migrations.AddField(
            model_name='alert',
            name='observer',
            field=models.ForeignKey(to='howl.Observer', verbose_name='Observer'),
        ),
    ]
