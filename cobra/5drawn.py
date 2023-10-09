from tkinter import *
from tkinter.messagebox import showinfo
import random

width = 800
height = 600
grid_width = 20

class Square:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
        self.color = color
        self.dim = [0, 0, 0, grid_width, grid_width, grid_width, grid_width, 0]
    
    def pos(self):
        return [self.dim[0] + self.x, self.dim[1] + self.y,
                self.dim[2] + self.x, self.dim[3] + self.y, 
                self.dim[4] + self.x, self.dim[5] + self.y,
                self.dim[6] + self.x, self.dim[7] + self.y]

class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title("Jogo da Cobra em Python")
        self.canvas = Canvas(self.window, bg="black", width=width, height=height)
        self.canvas.pack()

        # Criamos a cobra pedaço a pedaço
        s = Square(0, 20, 'yellow')        
        s1 = Square(0, 20, 'yellow')        
        s2 = Square(0, 20, 'yellow')        
        s3 = Square(0, 20, 'yellow')
        
        # Criamos uma fruta com posições x e y aleatórias e da cor azul
        f = Square(
                    # Posição X aleatória
                    random.randint(grid_width, (width / grid_width))*grid_width - grid_width,
                    
                    # Posição Y aleatória
                    random.randint(grid_width, (height / grid_width))*grid_width - grid_width,
                    
                    # Cor azul
                    'blue')
        
        self.window.mainloop()
        

g = Game()
g