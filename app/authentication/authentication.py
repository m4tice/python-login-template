"""
author: @GUU8HC
"""

from flask import render_template, jsonify

from app.authenticator import authenticator
from app.util import login_required, login_user, logout_user

from . import authentication_bp

@authentication_bp.route('/obsolete/signin')
def obsolete_signin():
    """
    route: /signin
    """
    return render_template('authentication/obsolete/signin.html')

@authentication_bp.route('/signin')
def signin():
    """
    route: /auth/signin
    """
    return render_template('authentication/signin.html')

@authentication_bp.route('/signin/<username>/<password>', methods=['GET'])
def authenticate(username, password):
    """
    route: /auth/signin/<username>/<password>
    """
    login_user(username)
    return jsonify({'result': authenticator.authenticate(username, password)})

@authentication_bp.route('/registration')
def registration():
    """
    route: /auth/registration
    """
    return render_template('authentication/registration.html')

@authentication_bp.route('/restore-password')
def restore_password():
    """
    route: /auth/restore-password
    """
    return render_template('authentication/restore-password.html')

@authentication_bp.route('/signout')
def signout():
    """
    route: /auth/signout
    """
    logout_user()
    return render_template('authentication/signin.html')
