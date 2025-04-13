"""
author: @guu8hc
"""

from flask import render_template, jsonify

from . import vocabulary_bp

@vocabulary_bp.route('/')
def vocabulary():
    """
    Vocabulary page
    """

    return render_template('vocabulary/vocabulary.html')

@vocabulary_bp.route('/data')
def get_data():
    """
    Vocabulary data
    """
    print("get_data")
    vocab_de_en = [
        ["Hallo", "Hello"],
        ["Welt", "World"]
    ]

    return jsonify({'pairs': vocab_de_en})
