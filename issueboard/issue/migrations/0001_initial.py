# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IssuePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
