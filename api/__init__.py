from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from .profile import ingredients
from .profile import dishes
