# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_auto_20150605_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailmatchplayer',
            name='team',
            field=models.ForeignKey(related_name='players', to='web_app.Team'),
        ),
    ]
