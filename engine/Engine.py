import tkinter as tk
from tkinter import ttk
from core.settings import *
from pathlib import Path
from PIL import Image, ImageTk

class Engine:

    def __init__(self):
        
        self.root = tk.Tk()
        """Game main screen"""
        self.root.title(GAME_NAME)
        self.root.state("zoomed")

        self.wx = self.root.winfo_screenwidth()
        """Window width"""
        self.wy = self.root.winfo_screenheight()
        """Window height"""

    def load_background(self,background_path:Path):
        """Load the background into main screen"""

        img_og = background_path.resize((self.wx, self.wy))
        img = ImageTk.PhotoImage(img_og)    

        background = tk.Label(self.root, image=img, bd=0)
        background.place(x=0, y=0, relwidth=1, relheight=1)

    def load_sprite(self,sprite_path:Path):
        import tkinter as tk

        img = tk.PhotoImage(file=sprite_path)

        label = tk.Label(self.root, image=img)
        label.pack()




    

    




    
        





