"""
author: @GUU8HC
"""

import hashlib

class Authenticator:
    """
    Authenticator class
    """
    def __init__(self, db):
        """
        *.db initialization
        """
        self.db = db

    def authenticate(self, username, password):
        """
        Authenticate user
        """
        _, _, userpwd = self.db.get_user_by_username(username)

        return userpwd == self.hash_password(password)

    def hash_password(self, password):
        """
        Hash password
        """
        return hashlib.sha256(password.encode()).hexdigest()
