# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20160726_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_time',
            field=models.TimeField(auto_now_add=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.TimeField(auto_now_add=True, auto_created=True),
        ),
    ]
