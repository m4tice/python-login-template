"""
author: @GUU8HC
"""
#pylint: disable=wrong-import-position
#pylint: disable=line-too-long

import hashlib

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
        return user[-1] == self.hash_password(password) if user else False

    def hash_password(self, password):
        """
        Return the SHA-256 hash of a password.

        Args:
            password (String): The provided password.

        Returns:
            String: The SHA-256 hash of the password.
        """
        return hashlib.sha256(password.encode()).hexdigest()
