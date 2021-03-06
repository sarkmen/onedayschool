# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QNA', '0002_auto_20160402_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=100)),
                ('question_content', models.TextField()),
                ('answer_title', models.CharField(max_length=200)),
                ('answer_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
