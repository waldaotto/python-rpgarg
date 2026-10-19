import sqlite3

class Database:

    def __init__(self):

        self._connection = sqlite3.connect("db/data.db")
        self._cursor = self.connection.cursor()
    
    @property
    def connection(self):
        return self._connection
    
    @property
    def cursor(self)->sqlite3.Cursor:
        return self._cursor


