from os import environ 

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')
RESUME_DIRECTORY_LOCATION = environ.get('RESUME_DIRECTORY_LOCATION')