# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emeetlyapp', '0008_auto_20171129_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potentialmatches',
            name='pmid',
            field=models.CharField(blank=True, max_length=26, null=True, unique=True),
        ),
    ]