# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20160726_0103'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
