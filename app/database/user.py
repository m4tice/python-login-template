"""
author: @GUU8HC
"""
# pylint: disable=wrong-import-position
# pylint: disable=line-too-long

from app.settings import DEBUG_MODE

from .db_interface import DBInterface

if DEBUG_MODE:
    FILE_NAME = "user.py"

class User(DBInterface):
    """
    User database operations
    """
    def __init__(self, db):
        super().__init__(db)
        self.table_user = "user"

    def get_all(self):
        """
        Get all users
        """
        query = f"SELECT * FROM {self.table_user};"

        if DEBUG_MODE:
            print(f"[DEBUG] {FILE_NAME}: get_all: {query}")

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_user_by_username(self, username):
        """
        Get user by username
        """
        query = f"SELECT * FROM {self.table_user} WHERE username = {username};"

        if DEBUG_MODE:
            print(f"[DEBUG] {FILE_NAME}: get_user_by_username: {query} with username: {username}")

        self.cursor.execute(query)
        result = self.cursor.fetchone()

        if DEBUG_MODE:
            print(f"[DEBUG] {FILE_NAME}: query_result: {result}")

        return result
