import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("GG Hub")
root.state("zoomed")  # Maximiza a janela no Windows

# Carrega e prepara a imagem
imagem_original = Image.open("background.jpg")

# Obtém o tamanho atual da janela
largura = root.winfo_screenwidth()
altura = root.winfo_screenheight()

imagem_original = imagem_original.resize((largura, altura))
imagem = ImageTk.PhotoImage(imagem_original)

# Cria o fundo
fundo = tk.Label(root, image=imagem, bd=0)
fundo.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()