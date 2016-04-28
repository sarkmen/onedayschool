import os
from .common import *

DEBUG=True
ALLOWED_HOSTS=['*']
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)
DATABASES = {
    'default': {
    'ENGINE': os.environ.get('DJANGO_DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
    'NAME': os.environ.get('DJANGO_DATABASE_NAME', 'ubuntu'),
    'USER': os.environ.get('DJANGO_DATABASE_USER', 'ubuntu'),
    'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', 'withaskdjango!'),
    'HOST': os.environ.get('DJANGO_DATABASE_HOST', '127.0.0.1'),
    # 소스코드에 민감한 정보 넣어놓으면 ㄴㄴ 그런데 그냥 넣어놈 환경변수 공부해서 처리하기
    }
}
DATABASE_OPTIONS = {'charset':'utf8'}
STATIC_ROOT= os.path.join(BASE_DIR, '..', 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
MEDIA_URL= '/media/'
