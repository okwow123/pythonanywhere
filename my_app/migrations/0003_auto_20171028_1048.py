# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20171028_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(default=None, null=True, upload_to=b'directory'),
        ),
        migrations.AlterField(
            model_name='post',
            name='no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
