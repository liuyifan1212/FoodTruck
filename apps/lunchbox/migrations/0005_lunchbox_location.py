# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchbox', '0004_auto_20180130_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunchbox',
            name='location',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
