# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20150522_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='food',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
