from BackpackModel import Backpack
from core.Model import Model

class Player(Model):
    """Player objetct"""

    def __init__(self):
        """Player creation:
        Args:
            name(str): player name;
        """
        self.COLUMNS = (
            "name",
            "role",
            "level",
            "life",
            "defense",
            "critic",
            "backpack",
            "status"
        )

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS player (
                            name TEXT NOT NULL UNIQUE,
                            role INT NOT NULL,
                            level NUMERIC NOT NULL,
                            life INT NOT NULL,
                            defense INT NOT NULL,
                            critic NUMERIC,
                            backpack INT NOT NULL,
                            status BOOLEAN NOT NULL CHECK (status IN (0, 1))
                            )""")

        self.db.connection.commit()
    
    @property
    def id(self)->int:
        return self._id

    @property
    def name(self)->str:
        return self._name
    
    @property.setter
    def name(self,name: str):
        self._name = name
        self.update(self.id,"name",name)

    @property
    def role(self):
        return self._role
    
    @property.setter
    def role(self,role):
        self._role = role
        self.update(self.id,"role",role)
        
    @property
    def level(self):
        return self._level
    
    @property.setter
    def level(self,level: float):
        self._level = level
        self.update(self.id,"level",level)
    
    @property
    def life(self):
        return self._life
    
    @property.setter
    def life(self,life: int):
        self._life = life
        self.update(self.id,"life",life)

    @property
    def defense(self):
        return self._defense
    
    @property.setter
    def defense(self,defense: int):
        self._defense = defense
        self.update(self.id,"defense",defense)
    
    @property
    def critic(self):
        return self._critic
    
    @property.setter
    def critic(self,critic: int):
        self._critic = critic
        self.update(self.id,"critic",critic)

    @property
    def backpack(self):
        return self._backpack
    
    @property.setter
    def backpack(self,backpack: int):
        self._backpack = backpack
        self.update(self.id,"backpack",backpack)

    @property
    def status(self):
        return self._status
    
    @property.setter
    def status(self,status: int):
        # 0 or 1
        self._status = status
        self.update(self.id,"status",status)

    @property
    def alive(self)->bool:
        """
        Returns:
            bool: if player is alive
        """
        
        if self.life <= 0:
            return False
        
        else:
            return True






    
    
