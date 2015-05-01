# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('steam_id', models.BigIntegerField()),
                ('community_visibility_state', models.IntegerField()),
                ('profile_state', models.IntegerField()),
                ('person_name', models.CharField(max_length=500)),
                ('last_logoff', models.BigIntegerField()),
                ('profile_url', models.CharField(max_length=500)),
                ('url_avatar', models.CharField(max_length=500)),
                ('url_avatar_medium', models.CharField(max_length=500)),
                ('url_avatar_full', models.CharField(max_length=500)),
                ('persona_state', models.IntegerField()),
                ('primary_clan_id', models.BigIntegerField()),
                ('time_created', models.BigIntegerField()),
                ('persona_state_flags', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='detailmatchplayer',
            name='player_account',
            field=models.ForeignKey(to='web_app.Account', null=True),
        ),
    ]
