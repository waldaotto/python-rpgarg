import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk


class Engine:

    def __init__(self, gamename: str):

        self.root = tk.Tk()
        """Game main screen"""

        self.root.title(gamename)
        self.root.state("zoomed")

        self.root.update_idletasks()

        self.wx = self.root.winfo_width()
        """Window width"""

        self.wy = self.root.winfo_height()
        """Window height"""

        self.canvas = tk.Canvas(
            self.root,
            highlightthickness=0,
            bd=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.imgs = []
        """Save image references"""

        self.sprites = {}
        """Store canvas sprite IDs"""

    def load_background(self, background_path: Path):
        """Load the background into the main screen."""

        img_og = Image.open(background_path).convert("RGBA")
        img_og = img_og.resize((self.wx, self.wy), Image.Resampling.LANCZOS)

        img = ImageTk.PhotoImage(img_og, master=self.root)

        self.imgs.append(img)

        background = self.canvas.create_image(
            0,
            0,
            image=img,
            anchor="nw",
            tags=("background",)
        )

        self.canvas.tag_lower(background)

        return background

    def load_sprite(
        self,
        sprite_path: Path,
        x: float,
        y: float,
        name: str | None = None
    ):
        """Load a sprite at the specified coordinates."""

        img = Image.open(sprite_path).convert("RGBA")
        sprite_img = ImageTk.PhotoImage(img, master=self.root)

        self.imgs.append(sprite_img)

        sprite_id = self.canvas.create_image(
            x,
            y,
            image=sprite_img,
            anchor="nw",
            tags=("sprite",)
        )

        if name is not None:
            self.sprites[name] = sprite_id

        return sprite_id

    def move(self, sprite: int, x: float, y: float):
        """Move a sprite to the specified coordinates."""

        self.canvas.coords(sprite, x, y)

    def move_sprite(
        self,
        event,
        sprite: int,
        move_speed: float
    ):
        """Move a sprite using the arrow keys."""

        x, y = self.canvas.coords(sprite)

        if event.keysym == "Up":
            y -= move_speed

        elif event.keysym == "Down":
            y += move_speed

        elif event.keysym == "Left":
            x -= move_speed

        elif event.keysym == "Right":
            x += move_speed

        self.move(sprite, x, y)

    def raise_sprite(self, sprite: int):
        """Bring a sprite to the foreground."""

        self.canvas.tag_raise(sprite)

    def lower_sprite(self, sprite: int):
        """Send a sprite to the background."""

        self.canvas.tag_lower(sprite)

    def run(self):
        """Start the game loop."""

        self.root.mainloop()