# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-01 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0003_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentoring',
            name='requirements',
            field=models.TextField(default=1, max_length=2000, verbose_name='멘토에게 바라는 점'),
            preserve_default=False,
        ),
    ]
