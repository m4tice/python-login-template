"""
author: @GUU8HC
"""
#pylint: disable=line-too-long

from app.settings import DEBUG_MODE

from .db_interface import DBInterface

class User(DBInterface):
    """
    User database operations
    """
    def __init__(self, db):
        super().__init__(db)
        self.table_user = "user"  # Updated table name

    def get_all(self):
        """
        Get all users
        """
        query = f"SELECT * FROM {self.table_user};"  # Updated table name

        if DEBUG_MODE:
            print(f"[DEBUG] user.py: get_all: {query}")

        self.cursor.execute(query)

        return self.cursor.fetchall()

    def get_user_by_username(self, username):
        """
        Get user by username
        """
        query = f"SELECT * FROM {self.table_user} WHERE username = '{username}';"  # Updated table name

        if DEBUG_MODE:
            print(f"[DEBUG] user.py: get_user_by_username: {query}")

        self.cursor.execute(query)

        return self.cursor.fetchone()
