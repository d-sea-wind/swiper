# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-03 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191127_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vip_end',
            field=models.DateTimeField(default='3000-1-1', verbose_name='会员过期时间'),
        ),
        migrations.AddField(
            model_name='user',
            name='vip_id',
            field=models.IntegerField(default=1, verbose_name='用户对应的会员 ID'),
        ),
    ]
