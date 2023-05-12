from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-o$vpn2t&268eln&a%)e^7%8u#l)ne37-$&wtsm@@7zexms02$x'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'province',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'mySQL@2023'
    }
}