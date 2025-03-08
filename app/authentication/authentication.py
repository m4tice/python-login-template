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

@authentication_bp.route('/loginv2')
def loginv2():
    """
    route: /auth/login
    """
    return render_template('authentication/loginv2.html')

@authentication_bp.route('/login/<username>/<password>', methods=['GET'])
def authenticate(username, password):
    """
    route: /auth/login/<username>/<password>
    """
    return jsonify({'result': True})

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