import os

from settings._from_dotenv import (
    _DEBUG,
    _SECRET_KEY,
)


ALLOWED_HOSTS: list[str] = []

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = _DEBUG

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "django_cv.urls"

SECRET_KEY = _SECRET_KEY

WSGI_APPLICATION = "django_cv.wsgi.application"
