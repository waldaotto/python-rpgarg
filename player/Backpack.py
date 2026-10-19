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

        bpk = self.find_by(column="player_id",value=player_id)[0]

        if bpk:

            self.id,self._player_id, self._slots = bpk
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
    



       

        








