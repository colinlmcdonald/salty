# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surfers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surfboard',
            name='model',
            field=models.ForeignKey(blank=True, to='surfers.SurfboardModel', null=True),
        ),
    ]
