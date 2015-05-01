# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_auto_20150501_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='person_name',
            new_name='persona_name',
        ),
    ]
