"""
Django settings for PPWuLiu project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

from django.contrib.messages import constants

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 创建日志的路径
LOG_PATH = os.path.join(BASE_DIR, "logs")
if not os.path.isdir(LOG_PATH):
    if os.path.isfile(LOG_PATH):
        os.remove(LOG_PATH)
    os.makedirs(LOG_PATH)

# 启用Django Debug Toolbar
ENABLE_DJANGO_TOOLBAR = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv("DJANGO_TMS_SECRET_KEY")
SECRET_KEY = '$rc35+clspfqjou0weyqxtehxi##6o9r7!5@hsqzsw$5g94bxa'
PBKDF2_ITERATIONS = 3

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'rest_framework',
    # 'django_filters',
    'wuliu.apps.WuliuConfig',
    'utils',
]
if DEBUG:
    try:
        import django_extensions
        INSTALLED_APPS.append('django_extensions')
        # print SQL queries in shell_plus
        SHELL_PLUS_PRINT_SQL = True
    except ImportError:
        pass

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Pyinstrument, 暂时不用, 因为Django Debug Toolbar更好用更强大
# if DEBUG:
#     try:
#         import pyinstrument
#         MIDDLEWARE.append('pyinstrument.middleware.ProfilerMiddleware')
#     except ImportError:
#         pass

# Django Debug Toolbar
if ENABLE_DJANGO_TOOLBAR:
    # debug_toolbar依赖于django.contrib.staticfiles
    if DEBUG and 'django.contrib.staticfiles' in INSTALLED_APPS:
        try:
            import debug_toolbar
            INSTALLED_APPS.append('debug_toolbar')
            MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
            # Internal IPs
            INTERNAL_IPS = [
                '127.0.0.1',
            ]
        except ImportError:
            pass

ROOT_URLCONF = 'PPWuLiu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wuliu.processor.pros'
            ],
        },
    },
]

WSGI_APPLICATION = 'PPWuLiu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.getenv("DJANGO_TMS_MYSQL_DATABASE_NAME"),
        # 'USER': os.getenv("DJANGO_TMS_MYSQL_USER"),
        # 'PASSWORD': os.getenv("DJANGO_TMS_MYSQL_PASSWORD"),
        # 'HOST': os.getenv("DJANGO_TMS_MYSQL_HOST"),
        # 'PORT': os.getenv("DJANGO_TMS_MYSQL_PORT"),

        'NAME': 'ppwuliu',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Custom

CACHES = {
    'default': {
        # 基于本地内存的缓存
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# 关闭浏览器使会话立即过期
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MESSAGE_TAGS = {
    constants.ERROR: "danger",
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        # Unused
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '%s/log.txt' % LOG_PATH,
            'encoding': 'utf-8',
        },
        'request_exceptions': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '%s/request_exceptions.txt' % LOG_PATH,
            'encoding': 'utf-8',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'wuliu.apps': {
            'handlers': ['request_exceptions'],
            'level': 'INFO',
            'propagate': True,
        },
        'utils.common.expire_lru_cache': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

'''
# channels相关配置, 暂时不用
ASGI_APPLICATION = "PPWuLiu.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        },
    },
}
'''