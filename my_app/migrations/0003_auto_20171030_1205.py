# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20171030_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default=b'test', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=b'content', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='good_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(default=None, null=True, upload_to=b'./my_app/static/upload'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=b'title', max_length=200, null=True),
        ),
    ]
