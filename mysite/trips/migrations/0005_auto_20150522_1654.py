# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20150522_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_spicy',
            new_name='relationship',
        ),
        migrations.RemoveField(
            model_name='post',
            name='price',
        ),
        migrations.AddField(
            model_name='post',
            name='habit',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
