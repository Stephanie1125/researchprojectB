# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('create_at', models.TimeField(auto_created=True, auto_now_add=True)),
                ('name', models.CharField(default='anonymous', max_length=100)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
