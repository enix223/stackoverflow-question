# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20170318_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]