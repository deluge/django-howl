# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howl', '0003_alert_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observer',
            name='operator',
            field=models.CharField(max_length=32, verbose_name='Operator type', choices=[('EqualOperator', 'Equals'), ('GreaterThanOperator', 'Greater than'), ('LowerThanOperator', 'Lower than')]),
        ),
    ]
