from pathlib import Path
import os
from conda.common._logic import TRUE

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY는 만들어진 그대로 두고 사용할 것
SECRET_KEY = 'ds@a8eqqzcjwzg=_%7mt-)%royhpj)i4mk76w6cis1_2hph&q5'  
# SECURITY WARNING: don't run with debug turned on in production!

# True로 세팅하면 개발모드, False로 세팅하면 운영모드
# False인 운영모드인 경우 아래 ALLOWED_HOSTS 리스트에 반드시 서버의 ip 혹의 도메인을 지정해야 함
# True인 개발 모드인 경우는 'localhost','127.0.0.1'로  간주함
DEBUG = True
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = '*'


# Application definition
# 새로운 앱이 만들어지면 이 자리에 등록해야 함
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark.apps.BookmarkConfig',
    'blog.apps.BlogConfig',
    'taggit.apps.TaggitAppConfig',
    'taggit_templatetags2',
    'widget_tweaks',
    'polls.apps.PollsConfig',
    'photo.apps.PhotoConfig',
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

# 프로젝트의 템플릿 파일이 위치할 디렉토리를 지정 (MVT == 스프링의 MVC 모델)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')], #os 패키지를 임포트해야함
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',   #src폴더안에 생긴 db.sqlite3
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr' #'en-us'

TIME_ZONE =  'Asia/Seoul' #'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True #타임존을 사용할 지 여부를 결정


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# 장고가 자동으로 만든 static들의 경로
STATIC_URL = '/static/'
# 우선적으로 써야할 것이 아래와 같이 statics 임의의 경로를 추가해서 사용할 수 있다
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

# 미디어 부분은 따로 추가 할 수 있다(추가한 부분임) 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

TAGGIT_CASE_INSENSITIVE = True
TAGGIT_LIMIT = 50

DISQUS_SHORTNAME = 'soyulmysite'
DISQUS_MY_DOMAIN = 'http://192.168.0.241'


#LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'