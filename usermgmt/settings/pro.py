from .base import *


DEBUG = True

ADMINS = (
    ('Brian C', 'chuyebrian577@gmail.com'),
)

ALLOWED_HOSTS = ["www.usermgmt.com", "usermgmt.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'TEST': {
            "NAME": BASE_DIR/ 'test_db.sqlite3',
        }
    }
}

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True