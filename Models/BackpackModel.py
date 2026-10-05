from core.Model import Model

class Backpack(Model):
    """Player backpack object"""

    def __init__(self):
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

        # foreign key item id

    @property
    def slots(self):
        ...

        
        

        
        


    
