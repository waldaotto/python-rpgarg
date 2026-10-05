from models.PlayerModel import Player
from core.Controller import Controller

class PlayerController(Controller):

    def __init__(self):
        self.MODEL = Player()
        self.VIEW = ...

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
