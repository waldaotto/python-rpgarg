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

        return self.cursor.execute(f"""SELECT item_id FROM {self.TABLE} WHERE backpack_id = ?""",(self.bpk_id)).fetchall()







