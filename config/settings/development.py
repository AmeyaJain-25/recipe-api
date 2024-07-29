from .base import *


DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'ec2-15-206-67-159.ap-south-1.compute.amazonaws.com' ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
