"""Application configuration defaults.

Values here are loaded by the Flask app factory and can be overridden by
environment variables or explicit ``create_app`` config overrides.
"""
from os import environ
from pathlib import Path
from sys import platform

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_RESOURCE_DIRECTORY = BASE_DIR / 'resources'

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')

RESOURCE_DIRECTORY = environ.get('RESOURCE_DIRECTORY', str(DEFAULT_RESOURCE_DIRECTORY))

_DEFAULT_RESUME_DIRECTORY = '/tmp' if platform == 'linux' else str(Path.home())
RESUME_DIRECTORY_LOCATION = environ.get('RESUME_DIRECTORY_LOCATION', _DEFAULT_RESUME_DIRECTORY)
RESUME_FILENAME = environ.get('RESUME_FILENAME', 'Derek Santos - Resume.docx')
RESUME_LOCATION = environ.get(
    'RESUME_LOCATION',
    str(Path(RESUME_DIRECTORY_LOCATION) / RESUME_FILENAME),
)

GENERATE_RESUME_ON_STARTUP = environ.get('GENERATE_RESUME_ON_STARTUP', 'true').lower() in {
    '1',
    'true',
    'yes',
    'on',
}
GITHUB_TIMEOUT_SECONDS = float(environ.get('GITHUB_TIMEOUT_SECONDS', '5'))
SPA_DIST_DIR = environ.get('SPA_DIST_DIR', str(BASE_DIR / 'static' / 'spa'))
