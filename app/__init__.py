"""
author: @GUU8HC
"""
#pylint: disable=import-outside-toplevel

from flask import Flask

from app.settings import DEBUG_MODE, USER_DB, SECRET_KEY, SESSION_COOKIE_HTTPONLY, SESSION_COOKIE_SECURE, SESSION_PERMANENT

def create_app():
    """
    function to create application
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    from app.home import home_bp
    app.register_blueprint(home_bp, url_prefix='/home')

    from app.authentication import authentication_bp
    app.register_blueprint(authentication_bp, url_prefix='/auth')

    return app
