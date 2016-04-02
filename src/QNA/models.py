from django.conf import settings
from django.core.files import File
from django.db import models
from django.utils import timezone

from accounts.models import Profile

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50, verbose_name='제목')
    content = models.TextField(verbose_name='질문내용')
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(verbose_name='답변')
    created_at = models.DateTimeField(auto_now_add=True)
