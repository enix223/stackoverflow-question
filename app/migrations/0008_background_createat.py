# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-26 03:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20161225_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='createAt',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 12, 26, 3, 59, 30, 989138, tzinfo=utc), verbose_name='create'),
            preserve_default=False,
        ),
    ]
