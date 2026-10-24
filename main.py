from pprint import pprint
from player.Player import Player
from player.Actions import Actions
from entities.Enemy import Enemy
from player.Backpack import Backpack
from player._item_bpk import _item_bpk
from engine.Engine import Engine
from core.settings import *
import tkinter as tk
import asyncio
from time import sleep


async def main():
    enemy = Enemy("mosntro",100,0,(3,5))
    player = Actions(Player("Pablo"))

    e = Engine(GAME_NAME)
    sprit = e.load_sprite(r"D:/PC/Desktop/python-rpgarg/assets/sprites/knight.png",100,200)
    e.load_background(r"D:\PC\Desktop\python-rpgarg\assets\background\wallpaerp.jpg")
    e.root.bind("<KeyPress>", lambda evt:e.move_sprite(evt,sprite=sprit,move_speed= int(FRAME_SPEED)))
    e.root.focus_set() 
    x = 100
    e.root.mainloop()
    
    
if __name__ == "__main__":
   asyncio.run( main())

