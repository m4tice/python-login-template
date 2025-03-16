"""
author: @GUU8HC
AI-generated test cases for the Home class in the home module.
"""
#pylint: disable=redefined-outer-name

import pytest
from flask import Flask
from app.authentication.authentication import authentication_bp


@pytest.fixture
def client():
    """
    Creates a Flask test client for the application.
    This function sets up a Flask application with the home blueprint registered
    and configures it for testing. It then yields a test client that can be used
    to simulate requests to the application.
    Yields:
        FlaskClient: A test client for the Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(authentication_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_signin_route(client):
    """Test the signin route."""
    response = client.get('/signin')
    assert response.status_code == 200
    print(f"[DEBUG] {response.data}")
    assert b'signin' in response.data

def test_registration_route(client):
    """Test the registration route."""
    response = client.get('/registration')
    assert response.status_code == 200
    print(f"[DEBUG] {response.data}")
    assert b'Registration' in response.data

def test_restore_password_route(client):
    """Test the restore-password route."""
    response = client.get('/restore-password')
    assert response.status_code == 200
    print(f"[DEBUG] {response.data}")
    assert b'Restore' in response.data
