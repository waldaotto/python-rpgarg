from pprint import pprint
from player.Player import Player
from player.Actions import Actions
from entities.Enemy import Enemy
from player.Backpack import Backpack
from player._item_bpk import _item_bpk


def main():
    enemy = Enemy("mosntro",100,0,(3,5))
    player = Actions(Player("Pablo"))

    enemy.attack(player)
    # player.backpack.put_item(1)
    # pprint(player.unequip_item(1))
    # print(player.backpack._itens())

    pprint(player.player.__dict__)

    
    

    
if __name__ == "__main__":
    main()

