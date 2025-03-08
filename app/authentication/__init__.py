"""
author: @GUU8HC
"""

from flask import Blueprint

authentication_bp = Blueprint('authentication', __name__, template_folder='templates', static_folder='static')

from . import authentication
