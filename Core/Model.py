from abc import ABC
from typing import Any

from db.Database import Database


class Model(ABC):
    """Base class for all database models.

    Subclasses must define the table name and its columns.

    Attributes:
        TABLE (str): Name of the table the model maps to.
        COLUMNS (tuple): Column names used for inserts (excluding `id`).
    """

    TABLE: str
    COLUMNS: tuple

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor

    def find_all(self) -> list[tuple]:
        """Fetch every record from the table.

        Warning:
            This may be slow on tables with many records.

        Returns:
            list[tuple]: All records, each one as a tuple.
        """
        self.cursor.execute(f"SELECT * FROM {self.TABLE}")
        return self.cursor.fetchall()

    def find(self, id: int) -> list[tuple]:
        """Fetch the record with the given id.

        Args:
            id (int): The record id.

        Returns:
            list[tuple]: A list with the matching record as a tuple,
            or an empty list if no record has that id.
        """
        self.cursor.execute(f"SELECT * FROM {self.TABLE} WHERE id = ?", (id,))
        return self.cursor.fetchall()

    def find_by(self,column:str,value:Any) -> list[tuple]:
        """Fetch the record by the column with the given value.

        Args:
            column (str): Column to search.
            value (Any): The value to find in column.

        Returns:
            list[tuple]: A list with the matching record as a tuple,
            or an empty list if no record has that value.
        """

        if not column in self.COLUMNS:
            raise KeyError(f'{column} doesnt exists in table.')

        self.cursor.execute(f"SELECT * FROM {self.TABLE} WHERE {column} = ?", (id,))
        return self.cursor.fetchall()

    def add(self, values: tuple) -> int:
        """Insert a new record into the table.

        Args:
            values (tuple): Values to insert, in the same order as `COLUMNS`.

        Returns:
            int: The id of the newly inserted record.
        """
        columns = ", ".join(self.COLUMNS)
        placeholders = ", ".join("?" for _ in values)

        self.cursor.execute(
            f"INSERT INTO {self.TABLE} ({columns}) VALUES ({placeholders})",
            values,
        )
        self.db.connection.commit()

        return self.cursor.lastrowid

    def add_many(self, rows: list[tuple]) -> int:
        """Insert several records at once.

        Args:
            rows (list[tuple]): Each tuple holds the values for one record,
                in the same order as `COLUMNS`.

        Returns:
            int: The number of records inserted.
        """
        columns = ", ".join(self.COLUMNS)
        placeholders = ", ".join("?" for _ in self.COLUMNS)

        self.cursor.executemany(
            f"INSERT INTO {self.TABLE} ({columns}) VALUES ({placeholders})",
            rows,
        )
        self.db.connection.commit()

        return self.cursor.rowcount

    def drop(self, id: int) -> int:
        """Delete the record with the given id.

        Args:
            id (int): The id of the record to delete.

        Returns:
            int: The id of the deleted record.
        """
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (id,))
        self.db.connection.commit()

        return id

    def update(self, id: int, column: str, value: Any) -> int:
        """Update a single column of the record with the given id.

        Args:
            id (int): The id of the record to update.
            column (str): The name of the column to update.
            value (Any): The new value for the column.

        Returns:
            int: The id of the updated record.
        """
        self.cursor.execute(
            f"UPDATE {self.TABLE} SET {column} = ? WHERE id = ?",
            (value, id),
        )
        self.db.connection.commit()

        return id