# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_time',
            field=models.TimeField(default=datetime.datetime(2016, 7, 26, 0, 58, 48, 124349)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.TimeField(default=datetime.datetime(2016, 7, 26, 0, 58, 48, 124289)),
        ),
    ]
