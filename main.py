
from player.Player import Player
from player.Actions import Actions
from entities.Enemy import Enemy
from player.Backpack import Backpack
from player._item_bpk import _item_bpk


def main():
    player = Player("Joao")
    action = Actions(player)
    action.equip_item(1)

    

    
if __name__ == "__main__":
    main()

