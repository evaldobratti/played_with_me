# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_auto_20150501_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_id',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
