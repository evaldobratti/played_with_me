# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0006_auto_20150606_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailmatch',
            name='match_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
