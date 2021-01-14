from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fps',
        'USER': 'fps',
        'PASSWORD': 'fps',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
