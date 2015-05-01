# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_auto_20150501_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='community_visibility_state',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_logoff',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='person_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='persona_state',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='persona_state_flags',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='primary_clan_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_state',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_url',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='time_created',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='url_avatar',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='url_avatar_full',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='url_avatar_medium',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
