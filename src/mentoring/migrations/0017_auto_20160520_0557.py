# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0016_auto_20160421_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menteefeedback',
            name='expect',
            field=models.TextField(max_length=2000, verbose_name='멘토링 받기 전에 기대하는 것이 있었나요? 그렇다면 어느 정도 해결되었나요?'),
        ),
        migrations.AlterField(
            model_name='menteefeedback',
            name='helpness',
            field=models.TextField(max_length=2000, verbose_name='이 프로그램을 통해 학교생활을 적극적으로 하는데 도움이 될 것 같은가요?'),
        ),
        migrations.AlterField(
            model_name='menteefeedback',
            name='impression',
            field=models.TextField(max_length=2000, verbose_name='오늘 멘토링을 받고 난 기분이 어떤가요?'),
        ),
        migrations.AlterField(
            model_name='menteefeedback',
            name='inconvinience',
            field=models.TextField(max_length=2000, verbose_name='아직 아쉬운 점이 있다면 질문으로 적어주세요.'),
        ),
        migrations.AlterField(
            model_name='menteefeedback',
            name='mentor_rating_reason',
            field=models.TextField(max_length=2000, verbose_name='멘토는 어떤 사람인가요? 어떤 점이 매력인가요?'),
        ),
        migrations.AlterField(
            model_name='menteefeedback',
            name='mentoring_rating_reason',
            field=models.TextField(max_length=2000, verbose_name='이 프로그램을 통해 얼마나 진로에 대해 이해할 수 있었나요?'),
        ),
        migrations.AlterField(
            model_name='menteefeedback',
            name='mirroring',
            field=models.TextField(max_length=2000, verbose_name='나는 멘토의 어떤 면을 닮고 싶은가요? 어떻게 하면 그 모습을 닮을 수 있을까요?'),
        ),
        migrations.AlterField(
            model_name='menteefeedback',
            name='onetime',
            field=models.TextField(max_length=2000, verbose_name='1회성 멘토 서비스에 만족하나요? 만일 지속적인 멘토링을 받고 싶다면 어떻게 운영되면 좋을까요?'),
        ),
        migrations.AlterField(
            model_name='menteefeedback',
            name='touring_rating_reason',
            field=models.TextField(max_length=2000, verbose_name='그 이유는 무엇인가요? 개선했으면 하는 점'),
        ),
        migrations.AlterField(
            model_name='menteefeedback',
            name='wannabe',
            field=models.TextField(max_length=2000, verbose_name='원하는 멘토상'),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='dream',
            field=models.TextField(max_length=2000, verbose_name='학생의 꿈은 무엇인가요?'),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='future_path',
            field=models.TextField(max_length=2000, verbose_name='학생이 원하는 진로와 그 진로를 택하게 된 근거. 그에 대한 멘토의 조언(행복과 연관지어)'),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='happiness',
            field=models.TextField(max_length=2000, verbose_name='학생은 언제 가장 행복해하나요?'),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='lifestyle',
            field=models.TextField(max_length=2000, verbose_name='학생의 생활패턴(시간 관리)분석 및 칭찬할 점과 보완했으면 하는 점'),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='reference',
            field=models.TextField(max_length=2000, verbose_name='집에서 학생을 지도할 때 참고했으면 하는 내용'),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='subjects',
            field=models.TextField(max_length=2000, verbose_name='학생이 가장 좋아하는 과목, 잘하는 과목, 부족한 과목은 무엇이고, 그 원인은 무엇인가요?'),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='sw',
            field=models.TextField(max_length=2000, verbose_name='학생의 장점 및 부족한 점(정서적 측면에서 토닥이며 학습 동기를 유발할 수 있도록)'),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='worry',
            field=models.TextField(max_length=2000, verbose_name='학생의 현재 가장 큰 고민은 무엇인가요?'),
        ),
        migrations.AlterField(
            model_name='mentoring',
            name='rating',
            field=models.CharField(max_length=40, verbose_name='성적수준'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='answering_question',
            field=models.TextField(max_length=2000, verbose_name='학생의 질문에 대한 답변'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='delivering_message',
            field=models.TextField(max_length=2000, verbose_name='그 외에 학생에게 전달하고 싶은 메시지'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='grade_manage',
            field=models.TextField(max_length=2000, verbose_name='내신 관리 비법'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='know_how',
            field=models.TextField(max_length=2000, verbose_name='기타 알려주고 싶은 본인만의 특별한 공부법'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='major_intro',
            field=models.TextField(max_length=2000, verbose_name='학과 소개'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='mentor_intro',
            field=models.TextField(max_length=2000, verbose_name='멘토 소개 문구'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='mentor_spec',
            field=models.TextField(max_length=2000, verbose_name='약 력'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='subject_study',
            field=models.TextField(max_length=2000, verbose_name='과목별 공부법'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='time_manage',
            field=models.TextField(max_length=2000, verbose_name='계획표 세우는 법'),
        ),
    ]
