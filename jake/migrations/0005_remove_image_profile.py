# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-20 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jake', '0004_auto_20200220_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]