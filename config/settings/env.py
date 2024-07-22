import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# used django environ 
# https://django-environ.readthedocs.io/en/latest/index.html
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = environ.Env(DEBUG=(bool, False))

DEBUG = env.bool('DEBUG')
SWAGGER = env.bool('SWAGGER')
S3_STORAGE = env.bool('S3_STORAGE')

MEDIA_BASE_URL = env('MEDIA_BASE_URL')
