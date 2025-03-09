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
    User database interface class.
    This class provides methods to interact with the user table in the database.
    Attributes:
        db: The database connection object.
        table_user (str): The name of the user table.
        Get all users from the user table.
        Returns:
            list: A list of tuples, each representing a user record.
        pass
        Get a user by their username.
        Args:
            username (str): The username of the user to retrieve.
        Returns:
            tuple: A tuple representing the user record, or None if no user is found.
        pass
    """
    def __init__(self, db):
        super().__init__(db)
        self.table_user = "user"

    def get_all(self):
        """
        Retrieves all records from the user table.
        Executes a SQL query to fetch all records from the user table and returns the result.
        Returns:
            list: A list of tuples representing all records in the user table.        
        """
        query = f"SELECT * FROM {self.table_user};"

        if DEBUG_MODE:
            print(f"[DEBUG] {FILE_NAME}: get_all: {query}")

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_user_by_username(self, username):
        """
        Retrieves a user record from the database by username.
        Args:
            username (str): The username of the user to retrieve.
        Returns:
            dict: A dictionary containing the user record if found, otherwise None.
        Raises:
            Exception: If there is an error executing the database query.
        """
        # Old implementation with risk when 'username' is [ admin' OR '1'='1 ]
        # query = f"SELECT * FROM {self.table_user} WHERE username = '{username}';"

        # if DEBUG_MODE:
        #     print(f"[DEBUG] {FILE_NAME}: get_user_by_username: {query} with username: {username}")

        # self.cursor.execute(query)
        # result = self.cursor.fetchone()

        # New implementation with SQL injection protection
        query = f"SELECT * FROM {self.table_user} WHERE username = ?;"

        if DEBUG_MODE:
            print(f"[DEBUG] {FILE_NAME}: get_user_by_username: {query} with username: {username}")

        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()

        if DEBUG_MODE:
            print(f"[DEBUG] {FILE_NAME}: query_result: {result}")

        return result
