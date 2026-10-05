from core.Model import Model

class Items(Model):

    def __init__(self):

        self.TABLE = "itens"
        self.COLUMNS = (
            "item",
            "description",
            "value"
        )

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS itens(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            item TEXT NOT NULL,
                            description TEXT NOT NULL,
                            value DECIMAL NOT NULL

                            )""")

        self.db.connection.commit()

