from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Database import Database

class Weapons:

    def __init__(self,db:Database):
        self.cursor = db.cursor
        self.db = db

        self._create_table()

    def _create_table(self):

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS weapons(
                            id INTEGER  PRIMARY KEY AUTOINCREMENT,
                            weapon VARCHAR(60) NOT NULL,
                            description TEXT NOT NULL,
                            damage_min INTEGER NOT NULL,
                            damage_max INTEGER NOT NULL,  
                            critic_min INTEGER NOT NULL  
                           );
                            """)
        self.db.connection.commit()
