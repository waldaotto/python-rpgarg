from core.Model import Model

class _item_bpk(Model):
    """Relation for itens in backpack"""

    def __init__(self,bpk_id:int):
        """Agrs:
            bpk_id (int): Backpack id    
        """
        super().__init__()

        self.COLUMNS = (
            'backpack_id',
            'item_id',
        )
        self.TABLE = "_item_bpk"

        self.bpk_id = bpk_id

        self._constructor(["INTEGER NOT NULL","INTEGER NOT NULL"])

    def get_itens(self)->list[int]:
        """Return all itens ID from backapck"""

        return self.cursor.execute(f"""SELECT item_id FROM {self.TABLE} WHERE backpack_id = ?""",(self.bpk_id,)).fetchall()
    
    def remove_one(self, item_id: int) -> bool:
        self.cursor.execute(
            f"""DELETE FROM {self.TABLE}
                WHERE rowid = (
                    SELECT rowid FROM {self.TABLE}
                    WHERE backpack_id = ? AND item_id = ?
                    LIMIT 1
                )""",
            (self.bpk_id, item_id),
        )

        if self.cursor.rowcount != 1:
            self.db.connection.rollback()
            return False 

        self.db.connection.commit()
        return True







