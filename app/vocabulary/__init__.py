"""
author: @guu8hc
"""
#pylint: disable=wrong-import-position, line-too-long

from flask import Blueprint

vocabulary_bp = Blueprint('vocabulary', __name__, template_folder='templates', static_folder='static')

from . import vocabulary
