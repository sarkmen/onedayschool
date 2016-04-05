# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0007_review_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentoring',
            old_name='major',
            new_name='major1',
        ),
        migrations.RemoveField(
            model_name='mentoring',
            name='area',
        ),
        migrations.AddField(
            model_name='mentoring',
            name='area_highschool',
            field=models.CharField(default=1, max_length=40, verbose_name='지역/학교'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='grade',
            field=models.CharField(default=1, max_length=20, verbose_name='학년'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='major2',
            field=models.CharField(default=1, max_length=40, verbose_name='전공선택/관심분야'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='major3',
            field=models.CharField(default=1, max_length=40, verbose_name='전공선택/관심분야'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='name',
            field=models.CharField(default=1, max_length=20, verbose_name='이름'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='phone_keeper',
            field=models.CharField(default=1, max_length=20, verbose_name='보호자 전화번호'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='phone_mentee',
            field=models.CharField(blank=True, max_length=20, verbose_name='학생 전화번호'),
        ),
        migrations.AddField(
            model_name='mentoring',
            name='questions',
            field=models.TextField(default=1, max_length=2000, verbose_name='평소 궁금했던 질문'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='rating',
            field=models.CharField(choices=[('높은 편', '높은 편'), ('중간 정도', '중간 정도'), ('낮은 편', '낮은 편'), ('매우 낮은 편', '매우 낮은 편')], default=1, max_length=20, verbose_name='성적수준'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='university',
            field=models.CharField(default=1, max_length=30, verbose_name='희망대학'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='wannabe',
            field=models.CharField(default=1, max_length=40, verbose_name='장래희망'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentoring',
            name='will_to_study',
            field=models.CharField(choices=[('높은 편', '높은 편'), ('중간 정도', '중간 정도'), ('낮은 편', '낮은 편'), ('매우 낮은 편', '매우 낮은 편')], default=1, max_length=30, verbose_name='공부의욕'),
            preserve_default=False,
        ),
    ]
