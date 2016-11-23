# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livechat', '0004_auto_20161124_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatboard',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatboard',
            name='room',
            field=models.CharField(default=b'anonymous', max_length=100),
        ),
    ]
