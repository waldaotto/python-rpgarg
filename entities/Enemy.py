from typing import TYPE_CHECKING
from random import randint

if TYPE_CHECKING:
    from player.Player import Player

class Enemy:
    
    def __init__(self,name:str,life:int,defense:int,attack:tuple):
        """
        Args:
            name (str): enemy name
            life (int): enemy life
            defense (int): enemy defense
            attack (tuple[int]): enemy damage (min,max)
        """

        if life < 1:
            raise ValueError("Enemy life cannot be negative or zero")

        if defense < 0:
            raise ValueError("Enemy defense cannot be negative")

        if not len(attack) == 2:
            raise ValueError("Attack must be a tuple with 2 integers; (int,int+)") 

        if not (isinstance(attack[0],int) or isinstance(attack[1],int)):
            raise ValueError("Attack must be a tuple with 2 integers; (int,int+)")

        if attack[1] < attack[0]:
            raise ValueError("Second value in attack must be greater than first one: (3,7)")

        self.name = name
        self.attack = attack
        self.life = life
        self.defense = defense
        self.alive = True

    def _is_dead(self)->bool:
        """Returns if enemy is dead"""

        return not self.alive

    def die(self):

        if self._is_dead():
            return

        self.alive = False
        self.life = 0

    def attack(self,player:type):

        if self._is_dead():
            return

        damage = randint(self.attack)
        player.damage(damage)

    def damage(self,damage:int):

        if self._is_dead():
            return

        if self.defense > damage:
            return
        
        total = self.life - (damage - self.defense)

        self.life = total

        if total < 1:
            self.die()

        

    

