# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20171028_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(default=None, upload_to=b'./my_app/static/upload'),
        ),
    ]
