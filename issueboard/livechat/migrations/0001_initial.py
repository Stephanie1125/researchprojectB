# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('name', models.CharField(max_length=100, default='anonymous')),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
