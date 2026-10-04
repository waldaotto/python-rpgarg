from abc import ABC
from db.Database import Database

class Model(ABC):
    """Base Model for models"""
    
    TABLE:str
    COLUMNS:tuple

    def __init__(self):

        self.db = Database()
        self.cursor = self.db.cursor

    def find_all(self)->list:
        """
        Returns:
            list: All registers, in tuple, in table (warning: it can take a litle time if many registers)
        """

        self.cursor.execute(f"""SELECT * FROM {self.TABLE}""")

        return self.cursor.fetchall()

    def find_by_id(self,id:int)->list:
        """
        Args:
            id(int): register id
        Returns:
            list: The register, in a tuple, with that id  

        """

        self.cursor.execute(f"""SELECT * FROM {self.TABLE} WHERE id = (?)""",(id,))

        return self.cursor.fetchall()

    def add(self,values:tuple)->int:
        """
        Args:
            values(tuple): Values to insert into table
        Returns:
            int: Last insert id
        """
        columns = ",".join(self.COLUMNS)
        print(columns)
        placeholders = ", ".join("?" for _ in values)
        print(placeholders)
        
        self.cursor.execute(f"""INSERT INTO {self.TABLE} ({columns}) values ({placeholders})""",values)
        self.db.connection.commit()

        return self.cursor.lastrowid
    
    def drop(self,id:int)->int:
        """
        Args:
            id(int): Item id to delete
        Returns:
            int: Deleted item id
        """

        self.cursor.execute(f"""DELETE FROM {self.TABLE} WHERE id = (?)""",(id,))
        self.db.connection.commit()

        return id
    
    def update(self,id:int,column:str,value:any)->int:
        """
        Args:
            id(int): Item id to update
            column(str): Table column to update
            value(any): New value for column
        Returns:
            int: Item id updated
        """

        self.cursor.execute(f"""UPDATE {self.TABLE} SET {column} = (?) WHERE id = (?)""",(value,id))
        self.db.connection.commit()

        return id





