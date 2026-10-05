from core.Model import Model

class Items(Model):

    def __init__(self):

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS items(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            item TEXT NOT NULL,
                            description TEXT NOT NULL,
                            role INT NOT NULL
                            )""")

        self.db.connection.commit()
        
