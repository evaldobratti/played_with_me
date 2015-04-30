# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ability_id', models.SmallIntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetailMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_radiant_win', models.BooleanField()),
                ('duration', models.BigIntegerField()),
                ('start_time', models.BigIntegerField()),
                ('match_id', models.BigIntegerField()),
                ('match_seq_num', models.BigIntegerField()),
                ('tower_status_radiant', models.SmallIntegerField()),
                ('tower_status_dire', models.SmallIntegerField()),
                ('barracks_status_radiant', models.SmallIntegerField()),
                ('barracks_status_dire', models.SmallIntegerField()),
                ('cluster', models.IntegerField()),
                ('cluster_name', models.CharField(max_length=50)),
                ('first_blood_time', models.IntegerField()),
                ('lobby_type', models.IntegerField()),
                ('lobby_name', models.CharField(max_length=50)),
                ('human_players', models.SmallIntegerField()),
                ('league_id', models.BigIntegerField()),
                ('positive_votes', models.IntegerField()),
                ('negative_votes', models.IntegerField()),
                ('game_mode', models.IntegerField()),
                ('game_mode_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DetailMatchAbilityUpgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.IntegerField()),
                ('upgraded_lvl', models.SmallIntegerField()),
                ('ability', models.ForeignKey(to='web_app.Ability')),
            ],
        ),
        migrations.CreateModel(
            name='DetailMatchPlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_id', models.BigIntegerField()),
                ('player_slot', models.SmallIntegerField()),
                ('kills', models.SmallIntegerField()),
                ('deaths', models.SmallIntegerField()),
                ('assists', models.SmallIntegerField()),
                ('leaver_status', models.BooleanField()),
                ('gold', models.IntegerField()),
                ('last_hits', models.SmallIntegerField()),
                ('denies', models.SmallIntegerField()),
                ('gold_per_min', models.SmallIntegerField()),
                ('xp_per_min', models.SmallIntegerField()),
                ('gold_spent', models.IntegerField()),
                ('hero_damage', models.IntegerField()),
                ('tower_damage', models.IntegerField()),
                ('hero_healing', models.IntegerField()),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetailMatchPlayerItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hero_id', models.SmallIntegerField()),
                ('localized_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('url_small_portrait', models.CharField(max_length=300)),
                ('url_large_portrait', models.CharField(max_length=300)),
                ('url_full_portrait', models.CharField(max_length=300)),
                ('url_vertical_portrait', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.SmallIntegerField()),
                ('localized_name', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('is_recipe', models.BooleanField()),
                ('in_secret_shop', models.BooleanField()),
                ('cost', models.SmallIntegerField()),
                ('in_side_shop', models.BooleanField()),
                ('url_image', models.CharField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='detailmatchplayeritem',
            name='item',
            field=models.ForeignKey(to='web_app.Item'),
        ),
        migrations.AddField(
            model_name='detailmatchplayeritem',
            name='player',
            field=models.ForeignKey(to='web_app.DetailMatchPlayer'),
        ),
        migrations.AddField(
            model_name='detailmatchplayer',
            name='hero',
            field=models.ForeignKey(to='web_app.Hero'),
        ),
        migrations.AddField(
            model_name='detailmatchplayer',
            name='match',
            field=models.ForeignKey(to='web_app.DetailMatch'),
        ),
        migrations.AddField(
            model_name='detailmatchabilityupgrade',
            name='player',
            field=models.ForeignKey(to='web_app.DetailMatchPlayer'),
        ),
    ]
