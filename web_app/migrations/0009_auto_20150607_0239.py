# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def migrate_teams(apps, schema_editor):
    DetailMatch = apps.get_model("web_app", "DetailMatch")
    for match in DetailMatch.objects.all():
        for player in match.radiant_team.players.all():
            player.match = match
            player.save()

        for player in match.dire_team.players.all():
            player.match = match
            player.save()

class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0008_detailmatchplayer_match'),
    ]

    operations = [
        migrations.RunPython(migrate_teams)
    ]
