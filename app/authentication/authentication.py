"""
author: @GUU8HC
"""

from flask import render_template, jsonify

from . import authentication_bp

@authentication_bp.route('/login')
def login():
    """
    route: /login
    """
    return render_template('authentication/login.html')

@authentication_bp.route('/login/<username>/<password>', methods=['GET'])
def authenticate(username, password):
    """
    route: /login/<username>/<password>
    """
    return jsonify({'result': True})
