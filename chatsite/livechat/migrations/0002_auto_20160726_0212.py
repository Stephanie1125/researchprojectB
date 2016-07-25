# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livechat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_at', models.TimeField(auto_created=True, auto_now_add=True)),
                ('name', models.CharField(default='anonymous', max_length=100)),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MessageBoard',
        ),
    ]
