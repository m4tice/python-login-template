"""
author: @GUU8HC
"""

from flask import render_template, jsonify

from app.authenticator import authenticator

from . import authentication_bp

@authentication_bp.route('/obsolete/login')
def obsolete_login():
    """
    route: /login
    """
    return render_template('authentication/obsolete/login.html')

@authentication_bp.route('/login')
def login():
    """
    route: /auth/login
    """
    return render_template('authentication/login.html')

@authentication_bp.route('/login/<username>/<password>', methods=['GET'])
def authenticate(username, password):
    """
    route: /auth/login/<username>/<password>
    """
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
