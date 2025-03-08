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

    return app
