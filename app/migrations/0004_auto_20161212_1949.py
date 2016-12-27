# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-13 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(max_length=50, verbose_name='the name of the author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name of the book'),
        ),
    ]
