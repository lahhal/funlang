# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-08 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-upload_date']},
        ),
    ]