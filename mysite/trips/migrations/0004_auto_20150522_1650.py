# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20150522_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_spicy',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
