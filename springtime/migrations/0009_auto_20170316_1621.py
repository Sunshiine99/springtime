# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-16 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('springtime', '0008_auto_20170316_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trampoline',
            name='broken',
            field=models.BooleanField(default=False),
        ),
    ]
