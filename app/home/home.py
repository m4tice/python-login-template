"""
author: @GUU8HC
"""

from flask import render_template

from . import home_bp

@home_bp.route('/')
def home():
    """
    Render the home page template.
    Returns:
        str: The rendered HTML of the home page.
    """
    return render_template('home/home.html')

@home_bp.route('/private')
def home_private():
    """
    Render the home page template.
    Returns:
        str: The rendered HTML of the home page.
    """
    return render_template('home/home-private.html')
