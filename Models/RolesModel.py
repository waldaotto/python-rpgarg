from core.Model import Model

class Roles(Model):

    def __init__(self):

        self.TABLE = "roles"
        self.COLUMNS = (
            "role",
            "description",
            "life_bonus",
            "defense_bonus",
            "critic_bonus"
        )

        self.cursor.execute("""CREATE TABLE roles(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            role TEXT NOT NULL,
                            description TEXT NOT NULL,
                            life_bonus INTEGER NOT NULL,
                            defense_bonus INTEGER NOT NULL,
                            critic_bonus NUMERIC NOT NULL
                            )""")
        self.db.connection.commit()
