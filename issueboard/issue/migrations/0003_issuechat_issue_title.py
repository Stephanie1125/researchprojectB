# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0002_issuechat'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuechat',
            name='issue_title',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
