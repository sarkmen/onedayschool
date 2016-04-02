from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.files import File
from django.db import models
from django.utils import timezone


from onedayschool.utils import random_name_upload_to, thumbnail
from accounts.models import Profile


# Create your models here.
MAJOR_CHOICES = (
    ('간호대학', '간호대학'),
    ('경영대학', '경영대학'),
    ('농경제사회학부', '농경제사회학부'),
    ('사회과학계열', '사회과학계열'),
    ('소비자아동학부', '소비자아동학부'),
    ('의류학과', '의류학과'),
    ('인문계열', '인문계열'),
    ('국어교육과', '국어교육과'),
    ('물리교육과', '물리교육과'),
    ('사회교육과', '사회교육과'),
    ('생물교육과', '생물교육과'),
    ('역사교육과', '역사교육과'),
    ('영어교육과', '영어교육과'),
    ('지구과학교육과', '지구과학교육과'),
    ('지리교육과', '지리교육과'),
    ('체육교육과', '체육교육과'),
    ('화학교육과', '화학교육과'),
    ('건축학과', '건축학과'),
    ('물리천문학부', '물리천문학부'),
    ('바이오시스템소재학부', '바이오시스템소재학'),
    ('산림과학부', '산림과학부'),
    ('생명과학부', '생명과학부'),
    ('수리과학부', '수리과학부'),
    ('식물생산과학부', '식물생산과학부'),
    ('식품영양학과', '식품영양학과'),
    ('응용생물화학부', '응용생물화학부'),
    ('화학부', '화학부'),
    ('건설환경공학부', '건설환경공학부'),
    ('기계항공공학부', '기계항공공학부'),
    ('산업공학과', '산업공학과'),
    ('식품동물생명공학부', '식품동물생명공학부'),
    ('재료공학부', '재료공학부'),
    ('전기정보공학부', '전기정보공학부'),
    ('조경지역시스템공학부', '조경지역시스템공학부'),
    ('조선해양공학과', '조선해양공학과'),
    ('컴퓨터공학부', '컴퓨터공학부'),
    ('화학생물공학부', '화학생물공학부'),
    ('의예과', '의예과'),

)



class Mentoring(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default='1')
    acceptor = models.ForeignKey(Profile, null=True)
    major = models.CharField(max_length=40, verbose_name='전공선택/관심분야')
    requirements = models.TextField(max_length=2000, verbose_name='멘토에게 바라는 점')
    date = models.CharField(max_length=20)
    capacity = models.PositiveSmallIntegerField(default=0)
    area = models.CharField(max_length=20, verbose_name='멘토링 지역')
    is_recommended = models.PositiveSmallIntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.author.username


class Plan(models.Model):
    mentoring = models.OneToOneField(Mentoring)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, default='1')
    major_intro = models.TextField(max_length=500, verbose_name='학과 소개')
    time_manage = models.TextField(max_length=500, verbose_name='계획표 세우는 법')
    grade_manage = models.TextField(max_length=500, verbose_name='내신 관리 비법')
    subject_study = models.TextField(max_length=500, verbose_name='과목 별 공부법')
    know_how = models.TextField(max_length=500, verbose_name='본인만의 특별한 공부법')
    delivering_message = models.TextField(max_length=500, verbose_name='그 외에 전달하고 싶은 메세지')



class Apply(models.Model):
    mentoring = models.ForeignKey(Mentoring)
    content = models.TextField()
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)





