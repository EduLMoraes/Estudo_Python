# biblioteca que gera a janela
from tkinter import *
from tkinter.messagebox import showinfo

# biblioteca pra gerar variaveis aleatórias
import random


# define o tamanho da janela
width = 800
height = 600

# define o tamanho da grade onde a cobra irá andar
grid_width = 20

# Gera um quadrado
class Square:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
        self.color = color
        self.dim = [0, 0, 0, grid_width, grid_width, grid_width, grid_width, 0]
    
    # retorna a posição do quadrado    
    def pos(self):
        return [self.dim[0] + self.x, self.dim[1] + self.y,
                self.dim[2] + self.x, self.dim[3] + self.y, 
                self.dim[4] + self.x, self.dim[5] + self.y,
                self.dim[6] + self.x, self.dim[7] + self.y]
    
    # define um valor para as velocidades    
    def setVel(self, newX, newY):
        self.velx = newX
        self.vely = newY
    
    # muda as posições dos quadrados    
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

# classe responsável para criar o jogo            
class Game:
    def __init__(self):
        # configurações da janela
        self.window = Tk()
        self.window.title("Jogo da cobra")
        self.canvas = Canvas(self.window, bg="black", width=width, height=height)
        self.canvas.pack()
        
        # cria a cobra inicialmente
        s = Square(0, 20, 'yellow')        
        s1 = Square(0, 20, 'yellow')        
        s2 = Square(0, 20, 'yellow')        
        s3 = Square(0, 20, 'yellow')
        
        # cria a fruta em formato de quadrado em uma posição aleatória
        f = Square(random.randint(grid_width, (width / grid_width))*grid_width - grid_width,
                           random.randint(grid_width, (height / grid_width))*grid_width - grid_width,
                           'blue')
        
        self.snake = [s, s1, s2, s3]
        self.food = [f]
        self.vel = [[20, 0], # velocidade primeiro quadrado 
                    [0, 0],  # posição do 2ª quadrado
                    [0, 0],  # posição do 3ª quadrado
                    [0, 0]]  # posição do 4ª quadrado      
        
        # Observa as setas do teclado
        self.window.bind("<Up>", self.moveUp)
        self.window.bind("<Down>", self.moveDown)
        self.window.bind("<Right>", self.moveRight)
        self.window.bind("<Left>", self.moveLeft)
    
    # Muda as velocidades para a direção desejada    
    def moveUp(self, event):
        if self.vel[0] != [0, 20]:
            self.vel[0] = [0, -20]
    
    def moveDown(self, event):
        if self.vel[0] != [0, -20]:
            self.vel[0] = [0, 20]
    
    def moveRight(self, event):
        if self.vel[0] != [-20, 0]:
            self.vel[0] = [20, 0]
    
    def moveLeft(self, event):
        if self.vel[0] != [20, 0]:
            self.vel[0] = [-20, 0]
            
    def run(self):
        count = 0
        
        while(True):
            self.canvas.delete('all')
            
            for i in range(len(self.vel) - 1, 0, -1):
                self.vel[i] = self.vel[i - 1] 
            
            for i in range(len(self.vel)):
                self.snake[i].velx = self.vel[i][0]
                self.snake[i].vely = self.vel[i][1]
            
            if(self.snake[0].pos() == self.food[0].pos()):
                self.food[0].x = random.randint(grid_width, (width/grid_width)) * grid_width - grid_width
                self.food[0].y = random.randint(grid_width, (height/grid_width)) * grid_width - grid_width
                self.vel.append([0, 0])
                self.snake.append(Square(self.snake[-1].x, self.snake[-1].y, self.snake[0].color))
            
            for s in self.snake:
                s.update()
                self.canvas.create_polygon(s.pos(), fill = s.color)
            
            for f in self.food:
                f.update()
                self.canvas.create_polygon(f.pos(), fill = f.color)
            
            for i in range(2, len(self.snake)):
                if count < 1:
                    count += 1
                elif self.snake[0].pos() == self.snake[i].pos():
                    showinfo(title = "Game Over", message = "GAME OVER!!!")
                    exit()
            
            self.canvas.after(70)
            self.window.update_idletasks()
            self.window.update()

g = Game()
g.run()