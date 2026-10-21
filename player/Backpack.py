from core.Model import Model
from player._item_bpk import _item_bpk
from player.Itens import Itens


class Backpack(Model):

    def __init__(self,player_id):
        super().__init__()
        self.TABLE = "backpack"
        self.COLUMNS = (
            'player_id',
            'slots',
        )

        self._constructor(["INTEGER NOT NULL","INTEGER NOT NULL",])
        self._loader(player_id)
        self.item_cursor = _item_bpk(self.id)
        self.itens_data = Itens()

    def _loader(self,player_id:int):

        bpk = self.find_by(column="player_id",value=player_id)

        if bpk:
            
            self.id,self._player_id, self._slots = bpk[0]
            return

        self.id, self._player_id,self._slots = self.add(values=(player_id,5)), player_id, 5
        return

    def _itens(self):
        """Return all id item record"""

        return self.item_cursor.get_itens()

    def item_info(self,item_id:int = None)->list[tuple]:
        """return specific item info or all itens.
        Args:
            item_id(int): Item ID if need one specific record
        """

        if item_id:
            return self.itens_data.find(item_id)[0]

        itens = []
        for id in self._itens:
            itens.append(self.itens_data.find(id)[0])

        return itens

    def put_item(self,item_id:int):
        """Put a item into backpack"""

        if self._is_full():
            raise KeyError(f"Backpack is already full")

        if not self._item_exists(item_id):
            raise ValueError(f"Item ID {item_id} does'nt exists")

        return self.item_cursor.add((self.id,item_id))

    def remove_item(self,item_id:int):
        """Remove a item from backpack"""

        if not self._item_exists(item_id):
            raise ValueError(f"Item ID {item_id} doesn't exists")

        if not self._in_backpack(item_id=item_id):
            raise ValueError(f"Item ID {item_id} isn't in backpack")

        return self.item_cursor.drop(item_id)


    def _is_full(self)->bool:
        """Answers if backpack is full"""

        self.item_cursor.cursor.execute(f"""SELECT COUNT(*) FROM {self.item_cursor.TABLE} WHERE backpack_id = ?""",(self.id,))
        total_itens = self.item_cursor.cursor.fetchone()[0]

        return True if total_itens >= self._slots else False

    def _item_exists(self,item_id:int)->bool:
        """Verify if item exists"""

        if self.itens_data.find(item_id):
            return True
        else:
            return False

    def _in_backpack(self,item_id:int)->bool:
        """Verify if item is in backpack"""

        self.item_cursor.cursor.execute(f"""SELECT COUNT(*) FROM {self.item_cursor.TABLE} WHERE backpack_id = ? AND item_id = ?""",(self.id,item_id))
        total_itens = self.item_cursor.cursor.fetchone()[0]

        return True if total_itens > 0 else False



        



       

        








