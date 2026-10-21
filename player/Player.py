from core.Model import Model
from player.Backpack import Backpack

class Player(Model):
    """Player object"""

    def __init__(self,username:str):
        """
        Args:
            name (str): Name of your carachter.
        """
        super().__init__()

        if len(username) > 30:
            raise ValueError("Name must have a lenght <30")
        # Init classs = logon 
        self.TABLE = 'player'
        self.COLUMNS = (
            'name',
            'life',
            'defense',
            'level',
            'xp',
            'honor',
            'slot0',
            'slot1',
            'slot2',
            'slot3',
            'slot4',
        )

        self.id = None
        self._name = ""
        self._life = 0
        self._defense = 0
        self._level = 0
        self._xp = 0
        self._honor = 0
        self.alive = True
        self._slot0 = None
        self._slot1 = None
        self._slot2 = None
        self._slot3 = None
        self._slot4 = None
        # self.backpack

        # first create db
        self._constructor([
            "TEXT UNIQUE NOT NULL",
            "INTEGER DEFAULT 10",
            "INTEGER DEFAULT 0",
            "INTEGER DEFAULT 0",
            "INTEGER DEFAULT 0",
            "INTEGER DEFAULT 0",
            "INTEGER",
            "INTEGER",
            "INTEGER",
            "INTEGER",
            "INTEGER",
        ])
        self._loader(name=username)

        self.backpack = Backpack(player_id=self.id)
        """Player backpack: itens"""

    def _loader(self,name:str):
        """Load player by name"""
        try:
                
            loaded_player = self.find_by(column='name',value=name)
            
            if not loaded_player:

                self.id = self.add((name,10,0,0,0,0,None,None,None,None,None))
                loaded_player = self.find(self.id)

            self.id,self._name, self._life, self._defense,self._level,self._xp,self._honor,self._slot0,self._slot1,self._slot2,self._slot3,self._slot4 = loaded_player[0]
        
        except Exception as e:

            raise Exception("Error on player loader", e)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) > 30:
            raise ValueError("Name must have at most 30 characters")

        self.update(self.id, "name", value)
        self._name = value

    @property
    def life(self) -> int:
        return self._life

    @life.setter
    def life(self, value: int):
        if value < 0:
            raise ValueError("Life cannot be negative")

        self.update(self.id, "life", value)
        self._life = value

    @property
    def defense(self) -> int:
        return self._defense

    @defense.setter
    def defense(self, value: int):
        if value < 0:
            raise ValueError("Defense cannot be negative")

        self.update(self.id, "defense", value)
        self._defense = value

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        if value < 0:
            raise ValueError("Level cannot be negative")

        self.update(self.id, "level", value)
        self._level = value

    @property
    def xp(self) -> int:
        return self._xp

    @xp.setter
    def xp(self, value: int):
        if value < 0:
            raise ValueError("XP cannot be negative")

        self.update(self.id, "xp", value)
        self._xp = value

    @property
    def honor(self) -> int:
        return self._honor

    @honor.setter
    def honor(self, value: int):
        self.update(self.id, "honor", value)
        self._honor = value

    # slot are int to receive an item id
    # if nul = non equiped
    @property
    def slot0(self):
        return self._slot0

    @slot0.setter
    def slot0(self, value: int):
        self.update(self.id, "slot0", value)
        self._slot0 = value
    @property
    def slot1(self):
        return self._slot1

    @slot1.setter
    def slot1(self, value: int):
        self.update(self.id, "slot1", value)
        self._slot1 = value

    @property
    def slot1(self):
        return self._slot1

    @slot1.setter
    def slot1(self, value: int):
        self.update(self.id, "slot1", value)
        self._slot1 = value

    @property
    def slot2(self):
        return self._slot2

    @slot2.setter
    def slot2(self, value: int):
        self.update(self.id, "slot2", value)
        self._slot2 = value

    @property
    def slot3(self):
        return self._slot3

    @slot3.setter
    def slot3(self, value: int):
        self.update(self.id, "slot3", value)
        self._slot3 = value

    @property
    def slot4(self):
        return self._slot4

    @slot4.setter
    def slot4(self, value: int):
        self.update(self.id, "slot4", value)
        self._slot4 = value

    def slots(self)->list[property]:
        """return array all itens"""

        return [self.slot0,
                self.slot1,
                self.slot2,
                self.slot3,
                self.slot4]