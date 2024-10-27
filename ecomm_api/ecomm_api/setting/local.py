from .base import *
from dotenv import load_dotenv


load_dotenv()
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('NAME'),
        'USER':os.environ.get('USER'),
        'PASSWORD':os.environ.get('PASSWORD'),
        'HOST':os.environ.get('HOST'),
        'PORT':os.environ.get('PORT'),
    }
    
}
