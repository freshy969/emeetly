# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-27 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emeetlyapp', '0006_auto_20171127_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notmatches',
            field=models.ManyToManyField(related_name='_user_notmatches_+', to='emeetlyapp.User'),
        ),
    ]
