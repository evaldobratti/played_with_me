# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0007_auto_20150606_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailmatchplayer',
            name='match',
            field=models.ForeignKey(related_name='players', to='web_app.DetailMatch', null=True),
        ),
    ]
