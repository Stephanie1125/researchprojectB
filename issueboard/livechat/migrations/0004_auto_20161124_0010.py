# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livechat', '0003_chatroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatboard',
            name='id',
        ),
        migrations.AlterField(
            model_name='chatboard',
            name='room',
            field=models.CharField(default=b'anonymous', max_length=100, serialize=False, primary_key=True),
        ),
    ]
