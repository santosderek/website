from flask import Blueprint

api = Blueprint('api_v1', __name__, url_prefix='/api/v1')

from . import github as github_routes
from . import resume as resume_routes
