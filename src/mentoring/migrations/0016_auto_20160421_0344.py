# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0015_auto_20160421_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='delivering_message',
            field=models.TextField(max_length=500, verbose_name='그 외에 학생에게 전달하고 싶은 메시지'),
        ),
    ]
