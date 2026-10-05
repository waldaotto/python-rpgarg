from core.Model import Model
from models.ItensModel import Itens

class Backpack(Model):
    """Player backpack object"""


    def __init__(self):
        self.TABLE = "backpack"
        self.CONN_TABLE = "backpack_item"

        self.COLUMNS = ("player_id",)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS backpack (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            player_id INTEGER NOT NULL
                            )
                        """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS backpack_item(
                            backpack_id INTEGER NOT NULL,
                            item_id INTEGER NOT NULL
                            )""")
                            
        self.db.connection.commit()

        self.Itens = Itens()

        # foreign key item id

    @property
    def slots(self):
        ...

    def get_itens(self)->list:
        """
        Returns:
            list: all itens linked to player´s backpack
        """

        self.cursor.execute(
            f"""
            SELECT i.*
            FROM {self.Itens.TABLE} AS i
            INNER JOIN {self.TABLE} AS b
                ON i.backpack_id = b.id
            """
        )

        return self.cursor.fetchall()

    
        
        

        
        


    
