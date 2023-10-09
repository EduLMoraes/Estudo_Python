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

        s = Square(0, 20, 'yellow')        
        s1 = Square(0, 20, 'yellow')        
        s2 = Square(0, 20, 'yellow')        
        s3 = Square(0, 20, 'yellow')
        
        f = Square(
                    random.randint(grid_width, (width / grid_width))*grid_width - grid_width,
                    random.randint(grid_width, (height / grid_width))*grid_width - grid_width,
                    'blue')
        
        # Juntamos todas os pedaços da cobra
        self.snake = [s, s1, s2, s3]
        
        # Formamos a comida
        self.food = [f]
        
        
    def run(self):
        # Criamos um loop infinito
        while(True):
            self.canvas.delete('all') # exclui tudo
            
            # Desenha a cobra    
            for s in self.snake:
                self.canvas.create_polygon(s.pos(), fill = s.color)
            
            # Desenha a comida
            for f in self.food:
                self.canvas.create_polygon(f.pos(), fill = f.color)
            
            # Mantém a janela aberta
            self.canvas.after(70)
            self.window.update_idletasks()
            self.window.update()    

g = Game()

# Passamos a chamar essa função para carregar a janela
g.run()