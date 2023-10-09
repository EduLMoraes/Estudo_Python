from tkinter import *
from tkinter.messagebox import showinfo
import random

width = 800
height = 600
grid_width = 20

# Criamos a classe chamada Square para criar os quadrados
class Square:
    def __init__(self, x, y, color): # Recebe os parâmetros x, y e color assim que iniciada
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
        self.color = color
        
        # Pegamos as dimensões e as colocamos como um vetor
        # para tornar o código mais fácil de entender
        self.dim = [0, 0, 0, grid_width, grid_width, grid_width, grid_width, 0]
    
    # Retorna a posição do quadrado com base nas dimensões da janela   
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
        self.window.mainloop()

g = Game()
g