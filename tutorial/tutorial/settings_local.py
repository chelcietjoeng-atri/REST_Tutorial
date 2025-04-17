INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "training_rest",
        "USER": "training_jkj",
        "PASSWORD": "training",
        "HOST": "localhost",
        "PORT": "",
    }
}

TIME_ZONE = 'America/Los_Angeles'