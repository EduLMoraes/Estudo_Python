from tkinter import *
from tkinter.messagebox import showinfo
import random

width = 800
height = 600
grid_width = 20

# Criamos a classe chamada Game
class Game:
    def __init__(self):
        
        # Atribuímos as configurações da janela
        self.window = Tk()
        
        # Colocamos um título em nossa janela
        self.window.title("Jogo da Cobra em Python")
        
        # Começamos a utilizar o Canvas para podermos desenhar na janela futuramente
        self.canvas = Canvas(self.window, bg="black", width=width, height=height)
        
        # Colocamos de fato o canvas na nossa janela a cobrindo inteira
        self.canvas.pack()
        
        # Começamos um loop que manterá a janela aberta
        self.window.mainloop()

# Construímos um objeto através da classe Game()
g = Game()

# Chamamos esse objeto e assim ele abre a janela
g