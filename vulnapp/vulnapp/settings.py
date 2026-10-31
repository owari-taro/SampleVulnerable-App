from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# INTENTIONALLY VULNERABLE: hardcoded secret, debug on, wildcard hosts
SECRET_KEY = "django-insecure-hardcoded-secret-key-1234567890"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "notes",
]

# INTENTIONALLY VULNERABLE: CSRF middleware removed, weak hasher
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"
SESSION_COOKIE_HTTPONLY = False

ROOT_URLCONF = "vulnapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "vulnapp.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
STATIC_URL = "/static/"
