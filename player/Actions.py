from player.Player import Player
from entities.Enemy import Enemy

class Actions:
    """Player actions"""

    def __init__(self,player: Player):
        """
        Args:
            player(Player): Player instance
        """
        
        if not isinstance(player):
            raise ValueError("Player parameter must be a instance")

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

    def attack(self,enemy:Enemy):
        
        ...

        

        



        
