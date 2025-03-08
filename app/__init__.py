"""
author: @GUU8HC
"""
#pylint: disable=import-outside-toplevel

from flask import Flask

def create_app():
    """
    function to create application
    """
    app = Flask(__name__)

    from app.home import home_bp
    app.register_blueprint(home_bp, url_prefix='/home')

    return app
