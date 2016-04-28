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

RATING_CHOICES = (
    ('아주 높은 편', '아주 높은 편'),
    ('높은 편', '높은 편'),
    ('중간 정도', '중간 정도'),
    ('낮은 편', '낮은 편'),
    ('아주 낮은 편', '아주 낮은 편')
)


class Mentoring(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default='1')
    acceptor = models.CharField(max_length=20, default='1', verbose_name='멘토 전화번호')
    capacity = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=20, verbose_name='이름')
    area_highschool = models.CharField(max_length=40, verbose_name='지역/학교')
    grade = models.CharField(max_length=20, verbose_name='학년')
    phone_mentee = models.CharField(max_length=20, blank=True, verbose_name='학생 전화번호')
    phone_keeper = models.CharField(max_length=20, verbose_name='보호자 전화번호')
    date = models.CharField(max_length=20, verbose_name='희망 날짜')
    wannabe = models.CharField(max_length=40, verbose_name='장래희망')
    university = models.CharField(max_length=30, verbose_name='희망대학')
    rating = models.CharField(max_length=20, verbose_name='성적수준')
    will_to_study = models.CharField(max_length=30, choices=RATING_CHOICES, verbose_name='공부의욕')
    major1 = models.CharField(max_length=40, verbose_name='관심전공1')
    major2 = models.CharField(max_length=40, verbose_name='관심전공2')
    major3 = models.CharField(max_length=40, verbose_name='관심전공3')
    questions = models.TextField(max_length=2000, verbose_name='평소 궁금했던 질문')
    requirements = models.TextField(max_length=2000, verbose_name='멘토에게 바라는 점')
    is_recommended = models.PositiveSmallIntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name+" ( "+self.author.username+" ) \b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b"+self.date



class Plan(models.Model):
    mentoring = models.OneToOneField(Mentoring)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, default='1')
    mentor_intro = models.TextField(max_length=500, verbose_name='멘토 소개 문구')
    mentor_spec = models.TextField(max_length=500, verbose_name='약 력')
    major_intro = models.TextField(max_length=500, verbose_name='학과 소개')
    time_manage = models.TextField(max_length=500, verbose_name='계획표 세우는 법')
    grade_manage = models.TextField(max_length=500, verbose_name='내신 관리 비법')
    subject_study = models.TextField(max_length=500, verbose_name='과목별 공부법')
    know_how = models.TextField(max_length=500, verbose_name='기타 알려주고 싶은 본인만의 특별한 공부법')
    answering_question = models.TextField(max_length=500, verbose_name='학생의 질문에 대한 답변')
    delivering_message = models.TextField(max_length=500, verbose_name='그 외에 학생에게 전달하고 싶은 메시지')

    def __str__(self):
        return self.mentor.profile.name + self.mentor.username


class Apply(models.Model):
    mentoring = models.ForeignKey(Mentoring)
    content = models.TextField()
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)


class Recommendmentor(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    major = models.CharField(max_length=40)
    career = models.CharField(max_length=100)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Review(models.Model):
    date = models.CharField(max_length=20)
    school = models.CharField(max_length=40)
    name = models.CharField(max_length=20)
    content = models.TextField()
    photo1 = models.ImageField(blank=True)
    photo2 = models.ImageField(blank=True)
    photo3 = models.ImageField(blank=True)
    photo4 = models.ImageField(blank=True)
    photo5 = models.ImageField(blank=True)
    photo6 = models.ImageField(blank=True)

    def __str__(self):
        return self.date + " " + self.school + " " +self.name+" 후기"


class Mentorfeedback(models.Model):
    mentoring = models.OneToOneField(Mentoring)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    dream = models.TextField(max_length=1000, verbose_name="학생의 꿈은 무엇인가요?")
    happiness = models.TextField(max_length=1000, verbose_name="학생은 언제 가장 행복해하나요?")
    worry = models.TextField(max_length=1000, verbose_name="학생의 현재 가장 큰 고민은 무엇인가요?")
    subjects = models.TextField(max_length=1000, verbose_name="학생이 가장 좋아하는 과목, 잘하는 과목, 부족한 과목은 무엇이고, 그 원인은 무엇인가요?")
    future_path = models.TextField(max_length=1000, verbose_name="학생이 원하는 진로와 그 진로를 택하게 된 근거. 그에 대한 멘토의 조언(행복과 연관지어)")
    lifestyle = models.TextField(max_length=1000, verbose_name="학생의 생활패턴(시간 관리)분석 및 칭찬할 점과 보완했으면 하는 점")
    sw =models.TextField(max_length=1000, verbose_name="학생의 장점 및 부족한 점(정서적 측면에서 토닥이며 학습 동기를 유발할 수 있도록)")
    reference = models.TextField(max_length=1000, verbose_name="집에서 학생을 지도할 때 참고했으면 하는 내용")

    def __str__(self):
        return self.mentoring.name


class Menteefeedback(models.Model):
    mentoring = models.OneToOneField(Mentoring)
    mentee = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    impression = models.TextField(max_length=500, verbose_name="오늘 멘토링을 받고 난 기분이 어떤가요?")
    expect = models.TextField(max_length=500, verbose_name="멘토링 받기 전에 기대하는 것이 있었나요? 그렇다면 어느 정도 해결되었나요?")
    inconvinience = models.TextField(max_length=500, verbose_name="아직 아쉬운 점이 있다면 질문으로 적어주세요.")
    touring_rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='투어 평점')
    touring_rating_reason = models.TextField(max_length=500, verbose_name="그 이유는 무엇인가요? 개선했으면 하는 점")
    mentor_rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='멘토 평점')
    mentor_rating_reason = models.TextField(max_length=500, verbose_name="멘토는 어떤 사람인가요? 어떤 점이 매력인가요?")
    mirroring = models.TextField(max_length=500, verbose_name="나는 멘토의 어떤 면을 닮고 싶은가요? 어떻게 하면 그 모습을 닮을 수 있을까요?")
    wannabe = models.TextField(max_length=500, verbose_name="원하는 멘토상")
    mentoring_rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='멘토링 평점')
    mentoring_rating_reason = models.TextField(max_length=500, verbose_name="이 프로그램을 통해 얼마나 진로에 대해 이해할 수 있었나요?")
    helpness = models.TextField(max_length=500, verbose_name="이 프로그램을 통해 학교생활을 적극적으로 하는데 도움이 될 것 같은가요?")
    onetime= models.TextField(max_length=500, verbose_name="1회성 멘토 서비스에 만족하나요? 만일 지속적인 멘토링을 받고 싶다면 어떻게 운영되면 좋을까요?")

    def __str__(self):
        return self.mentoring.name



class Mentoring_question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50, verbose_name='제목')
    content = models.TextField(verbose_name='질문내용')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Mentoring_answer(models.Model):
    question = models.ForeignKey(Mentoring_question)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(verbose_name='답변')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question.title


class Mentoring_faq(models.Model):
    question_title = models.CharField(max_length=100)
    question_content = models.TextField()
    answer_title = models.CharField(max_length=200)
    answer_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_title

