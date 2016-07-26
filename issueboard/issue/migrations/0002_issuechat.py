# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueChat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('name', models.CharField(default='anonymous', max_length=100)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
