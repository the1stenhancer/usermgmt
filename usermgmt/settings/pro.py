from .base import *


DEBUG = False

ADMINS = (
    ('Brian C', 'chuyebrian577@gmail.com'),
)

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'TEST': {
            "NAME": BASE_DIR/ 'test_db.sqlite3',
        }
    }
}