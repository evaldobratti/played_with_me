# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_auto_20150607_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailmatch',
            name='dire_team',
        ),
        migrations.RemoveField(
            model_name='detailmatch',
            name='radiant_team',
        ),
        migrations.RemoveField(
            model_name='detailmatchplayer',
            name='team',
        ),
        migrations.AlterField(
            model_name='detailmatchplayer',
            name='match',
            field=models.ForeignKey(related_name='players', to='web_app.DetailMatch'),
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
