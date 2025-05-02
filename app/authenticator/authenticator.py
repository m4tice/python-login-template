"""
author: @GUU8HC
"""
#pylint: disable=wrong-import-position
#pylint: disable=line-too-long

import hashlib
from bcrypt import checkpw, gensalt, hashpw

from app.database.user import User

class Authenticator:
    """
    Authenticator class
    """
    def __init__(self, db: User):
        """
        Initializes the Authenticator with a database connection.
        Args:
            db: The database connection object.
        """
        self.db = db

    def hash_password(self, password):
        """
        Return the SHA-256 hash of a password.

        Args:
            password (String): The provided password.

        Returns:
            String: The SHA-256 hash of the password.
        """
        # return hashlib.sha256(password.encode()).hexdigest()
        return hashpw(password.encode(), gensalt()).decode('utf-8')

    def verify_password(self, password, hashed_password):
        """
        Verifies if the provided password matches the hashed password.
        Args:
            password (str): The plain text password to verify.
            hashed_password (str): The hashed password to compare against.
        Returns:
            bool: True if the password matches the hashed password, False otherwise.
        """
        return checkpw(password.encode(), hashed_password.encode())

    def authenticate(self, username, password):
        """
        Authenticate user.
        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        # Get user by username
        # return None if user does not exist in the database
        user = self.db.get_user_by_username(username)

        # Perform password validation if user exists
        # return user[-1] == self.hash_password(password) if user else False
        return self.verify_password(password, user[-1]) if user else False

    def register(self, username, password):
        """
        Register a new user.
        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        Returns:
            bool: True if registration is successful, False otherwise.
        """
        # Check if user already exists
        if self.db.get_user_by_username(username):
            return False

        # Create new user
        self.db.create_user(username, self.hash_password(password))
        return True
