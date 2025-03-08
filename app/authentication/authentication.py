"""
author: @GUU8HC
"""

from flask import render_template

from . import authentication_bp

@authentication_bp.route('/login')
def login():
    """
    route: /login
    """
    return render_template('authentication/loginv2.html')