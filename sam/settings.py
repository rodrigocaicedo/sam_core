#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django settings for sam project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&_jvoudkepngg4qqtiu_ex9uya7(8m_wjl4_rm*--^05fwl2fn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.99.20.125', 'server1.divergente.ec', 'canaldocente.montebelloacademy.org']

AUTH_USER_MODEL = 'usuarios_sam.CustomUser'


AUTHENTICATION_BACKENDS = [
    "usuarios_sam.authbackend.Office365Backend",
    'django.contrib.auth.backends.ModelBackend',
    
]

LOGIN_URL = '/user/login'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios_sam',
    'capellania_sam',
	'admisiones_sam',
    "comunicaciones_sam",
    "uniformes_sam",
    "biblioteca_sam",
    "general_sam",
    "secretaria_sam",
    "facturacion_sam",
    'personal_sam',
    'canales_sam',
    "socioeco_sam",
    'django_countries',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'tinymce', 
    'sslserver',
    "mailqueue",
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

SITE_ID = "3"

ROOT_URLCONF = 'sam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "general_sam.processors.schoolyear",
                "general_sam.processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'sam.wsgi.application'

MAILQUEUE_CELERY = True

MAILQUEUE_QUEUE_UP = False

#CELERY_ROUTES = {"comunicaciones_sam.tasks.send_mail": {"queue": "comunicaciones_sam"}}

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sam_prod',
        'USER': 'sam',
        'PASSWORD': 'Alangasi6021',
        'HOST': 'localhost',
        'PORT':'',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'comunicaciones@montebelloacademy.org'
EMAIL_HOST_PASSWORD = 'Alangasi6021'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-ec'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = "/var/www/django_projects/sam_prod/statics/"

MEDIA_ROOT = "/var/www/django_projects/sam_prod/uploads/"  

MEDIA_URL = "/uploads/"

STATIC_URL = '/static/'



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
#    '/var/www/static/',
]
