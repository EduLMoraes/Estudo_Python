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

    # Atualiza o valor da posição do quadrado   
    def setVel(self, newX, newY):
        self.velx = newX
        self.vely = newY
    
    # Atualiza o quadrado
    def update(self):
        if self.x > 0 and self.x < width-grid_width:
            self.x += self.velx
        if self.y > 0 and self.y < height-grid_width:
            self.y += self.vely
        if self.x == 0 and self.velx > 0:
            self.x += self.velx
        if self.x == width-grid_width and self.velx < 0:
            self.x += self.velx
        if self.y == 0 and self.vely > 0:
            self.y += self.vely
        if self.y == height-grid_width and self.vely < 0:
            self.y += self.vely

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
        
        self.snake = [s, s1, s2, s3]
        self.food = [f]
        
        # Definimos a velocidade dos quadrados da cobra
        self.vel = [[20, 0], # velocidade primeiro quadrado 
                    [0, 0],  # posição do 2ª quadrado
                    [0, 0],  # posição do 3ª quadrado
                    [0, 0]]  # posição do 4ª quadrado
        
    def run(self):
        while(True):
            self.canvas.delete('all')
            
            # Move um o primeiro quadrado da cobra
            for i in range(len(self.vel)):
                self.snake[i].velx = self.vel[i][0]
                self.snake[i].vely = self.vel[i][1]
            
            for s in self.snake:
                # Atualiza a posição da cobra
                s.update()
                self.canvas.create_polygon(s.pos(), fill = s.color)
            
            for f in self.food:
                # Atualiza a posição da fruta
                f.update()
                self.canvas.create_polygon(f.pos(), fill = f.color)
            
            self.canvas.after(70)
            self.window.update_idletasks()
            self.window.update()    

g = Game()
g.run()