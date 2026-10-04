class Player:
    """Player objetct"""

    def __init__(self,name: str = "Joe"):
        """Player creation:
        Args:
            name(str): player name;
        """
        
        self._name = name
        """Player name"""
        self._role = None
        """Player role; define your attack type."""
        self._level = 0
        """Player level; grow your stats."""
        self._life = 20
        """Player life; how much you can be hurt."""
        self._defense = 4
        """Player defense; Minimun attack to hit you."""
        self._attack = 1
        """Player attack; multiplie your attack by X."""
    
    @property
    def name(self):
        return self._name
    
    @property.setter
    def name(self,name: str="Joe"):
        self._name = name

    @property
    def role(self):
        return self._role
    
    @property.setter
    def role(self,role):
        self._role = role
        
    @property
    def level(self):
        return self._level
    
    @property.setter
    def level(self,level: float):
        self._level = level
    
    @property
    def life(self):
        return self._life
    
    @property.setter
    def life(self,life: int):
        self._life = life

    @property
    def defense(self):
        return self._defense
    
    @property.setter
    def defense(self,defense: int):
        self._defense = defense
    
    @property
    def attack(self):
        return self._attack
    
    @property.setter
    def attack(self,attack: int):
        self._attack = attack
    

    


    
    
