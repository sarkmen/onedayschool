# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-16 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160404_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='highschool',
            field=models.CharField(blank=True, max_length=40, verbose_name='출신 고등학교'),
        ),
    ]