from flask import Blueprint

api = Blueprint('api_v1', __name__, url_prefix='/api/v1')

from .resume import *