from models.PlayerModel import Player
from core.Controller import Controller
import pandas as pd

class PlayerController(Controller):

    def __init__(self):
        self.MODEL = Player()

    def load_player(self,name:str):

        data = self.MODEL.find_all()
        df = (pd.DataFrame(data,columns=self.MODEL.COLUMNS))
        player = df[df['name'] == name]

        if player.empty:
            ...
        
        dictPlayer = player.to_dict(orient='records')[0]

        self.MODEL.name = dictPlayer["name"]
        self.MODEL.role = dictPlayer["role"]
        self.MODEL.level = dictPlayer["level"]
        self.MODEL.life = dictPlayer["life"]
        self.MODEL.defense = dictPlayer["defense"]
        self.MODEL.critic = dictPlayer["critic"]
        self.MODEL.backpack = dictPlayer["backpack"]
        self.MODEL.status = dictPlayer["status"]
        
    def create_player(self,name:str,role:int)->int:
        # need roles to receive bonus 
        ...



    def take_damage(self,damage:int)-> bool:
        """
        Reduce the damage from life, including defense.
        Args:
            damage(int): damage to take
        Returns:
            bool: if is alive or not
        """

        diff = self.MODEL.life - abs((damage - self.MODEL.defense))

        if diff <= 0:
            self.die()
            return

        self.MODEL.life = diff
        

        return self.MODEL.alive
    
    def die(self):
        
        if not self.MODEL.alive:
            self.MODEL.status = 0
            self.MODEL.life = 0

    def hit(self,enemy:type):
        ...
