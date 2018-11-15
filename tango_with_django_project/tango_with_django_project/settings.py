"""
Django settings for tango_with_django_project project.

Generated by 'django-admin startproject' using Django 1.9.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')          #指向BASE_DIR目录下的templates目录，另外拼接系统路径一定要使用os.path.join()函数，目的是使用正确的路径分隔符，因为不同操作系统的路径分隔符不一样。
STATIC_DIR = os.path.join(BASE_DIR, 'static')   #指向BASE_DIR目录下的static目录
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [STATIC_DIR, ]   #这个数据结构的值是一系列路径，让Django在其中寻找要伺服的静态文件

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'za@f8itc$a0s!5==1d@n2@tt*&cbn5%sm07uggw%*mk$3zzl##'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # 用于访问Django提供的身份验证系统
    'django.contrib.contenttypes',  # 供auth应用跟踪数据库中的模型
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tango_with_django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],      #告诉Django模板在何处(这里要使用绝对路径) eg:'<workspace>/tango_with_django_project/templates'
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',  #后添加的上下文处理器
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),   #BASE_DIR是setting.py文件所在目录的路径,用到了Python的特殊属性__file__，指的是所在文件的绝对路径
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

# 密码验证器 每个验证器都有OPTIONS 字典(便于自定义)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': { 'min_length': 8, }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/' #指定启动Django开发服务器通过什么URL访问静态文件 现在是http://127.0.0.1:8000/static/

MEDIA_ROOT = MEDIA_DIR  #告诉Django在哪里寻找上传的媒体文件
MEDIA_URL = '/media/' #指明通过什么URL伺服媒体文件

# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)

# Password Hash
# 哈希算法的顺序很重要，Django将使用PASSWORD_HASHERS 中的第一个哈希算法(setting.PASSWORD_HASHERS[0])
# 更安全的哈希算法 pip install bcrypt (SHA256)
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
)