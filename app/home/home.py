"""
author: @GUU8HC
"""

from flask import render_template

from . import home_bp

@home_bp.route('/')
def home():
    """
    route: /home
    """
    return render_template('home/home.html')
