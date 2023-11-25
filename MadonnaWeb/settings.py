"""
Django settings for MadonnaWeb project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from email.policy import default
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ks^@f@n7+(yn=n-5!k$od+3^1x+fyl41qqudvdq@q4jzjwq_a9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["139.162.7.135", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "Home",
    "Reservation",
    "users.apps.UsersConfig",
    "blog",
    "Reservation.reservation_function",
    "Reports",
    "Reports.scripts",
    "django.contrib.humanize",
    "test",
    "captcha",
    "admin_datta.apps.AdminDattaConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_session_timeout.middleware.SessionTimeoutMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimila‌​rityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValida‌​tor",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValid‌​ator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordVali‌​dator",
    },
]

ROOT_URLCONF = "MadonnaWeb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "static/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
MEDIA_ROOT = BASE_DIR / "Media"
MEDIA_URL = ""
WSGI_APPLICATION = "MadonnaWeb.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", default="db_name"),
        "USER": os.getenv("DB_USER", default="dbb_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", default="db_password"),
        "HOST": os.getenv("DB_HOST", default="db_host"),
        "PORT": os.getenv("DB_PORT", default="5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Manila"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

LOGIN_REDIRECT_URL = "home"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = "/staff"
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
# SESSION_COOKIE_AGE = 30 * 60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_EXPIRE_SECONDS = 1800  # Expire after 30 minutes
SESSION_TIMEOUT_REDIRECT = "login"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587  # Use port 587 for TLS
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = "dmanedward1110@gmail.com"  # Your Gmail email address
EMAIL_HOST_PASSWORD = "mvxp nfkd leqz auez"

RECAPTCHA_SSL_VERIFICATION = False
RECAPTCHA_PUBLIC_KEY = "6Lf4l0koAAAAAATJKiQvaGcslQKOVXl438opgZcP"
RECAPTCHA_PRIVATE_KEY = "6Lf4l0koAAAAAKF_xyoPOCTvijyScPNEJD1ABs38"

PAYMONGO_PUBLIC_KEY = "pk_test_V35HwBEoyZRya4WP5jhYj9rY"
PAYMONGO_SECRET_KEY = "sk_test_ttWkBkczoDgX6dJ2T5fJndVm"

# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

TIME_INPUT_FORMATS = ("%I:%M %p",)
