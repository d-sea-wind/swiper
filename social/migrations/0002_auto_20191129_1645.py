# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-29 16:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('uid1', 'uid2')]),
        ),
    ]