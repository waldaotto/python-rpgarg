
from Core.Model import Model


class Item(Model):

    TABLE = "banana"
    COLUMNS = ("nome",)

    def c(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS banana(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(20)
        )""")


    
print(Item().find_by_id(1))


