from os import environ
from .base import *

DEBUG = True
SECRET_KEY = environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['*']
