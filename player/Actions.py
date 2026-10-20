from player.Player import Player
from entities.Enemy import Enemy
from player.Itens import *
from random import randint

class Actions:
    """Player actions"""

    def __init__(self,player: Player):
        """
        Args:
            player(Player): Player instance
        """

        self.player = player
    
    def _is_dead(self)->bool:
        """Returns if player is dead"""

        return not self.player.alive

    def die(self):
        """turn player dead"""

        if self._is_dead():
            return

        try: 
            self.player.life = 0
        except Exception as e:
            print("Error dying: "+e)
            return

        self.player.alive = False

    def damage(self,damage:int)->int:
        """Reduce life from player
        Args:
            damage (int): How much damage player will take
        Returns:
            int: Player's life left
        """

        if self._is_dead():
            return

        if self.player.defense > damage:
            return

        try:
            left = self.player.life - (damage - self.player.defense)

            if left <= 0:
                self.die()
                return 0
            
            self.player.life -= damage
            return self.player.life
        except Exception as e:
            print("Error damage: "+e)
            return

    def attack(self,enemy:Enemy,attack_dmg: int = 0)->int:
        """Attack an enemy
        Args:
            enemy (enemy): Enemy to attack.
            attack_dmg (int): External attack dmg
        Returns:
            int: Enemy's life
        """
        
        slots = self.player.slots()
        lf = enemy.life

        for item in slots:
            if not item:
                continue

            item_id,item_name,item_type,item_value,item_price = item
            if item_type == 1:
                attack_dmg += self._randomize_damage(item_value)

        enemy.damage(attack_dmg)
        print(f"{self.player.name} attacked Enemy {enemy.name} and caused: Enemy: -{lf-enemy.life}")
        return enemy.life 

    def _randomize_damage(self,damage:int)->int:
        """Helper to randomize the item damage"""

        return randint((damage - ((damage/100)*25)),(damage + ((damage/100)*25)))


        

        



        
