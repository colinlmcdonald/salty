# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surfers', '0002_surfboard_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surfboard',
            old_name='model',
            new_name='surfboard_model',
        ),
    ]
