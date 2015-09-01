# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20150522_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
