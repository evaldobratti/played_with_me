# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_account_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='steam_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
