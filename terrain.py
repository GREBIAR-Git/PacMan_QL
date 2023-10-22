import numpy as np 
import pygame

class Map:
    def __init__(self, width, height):        
        self.matrix = np.array([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 6, 1, 2, 1, 0, 1, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 1, 0, 1, 2, 1, 6, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 1],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 4, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 4, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1, 0, 1, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 1, 0, 1, 2, 2, 2, 1],
            [1, 2, 2, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 4, 0, 4, 1, 2, 2, 2, 2, 2, 2, 2, 1, 4, 0, 4, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 1],
            [1, 2, 2, 2, 1, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 1],
            [1, 6, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 6, 1],
            [1, 0, 0, 0, 1, 4, 0, 4, 0, 0, 0, 4, 3, 4, 0, 0, 0, 4, 0, 4, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
        self.width = width
        self.height = height
        self.score = 0
        self.scoreWin = 0
        for x in range(25):
            for y in range(25):
                if(self.matrix[x,y]==0 or self.matrix[x,y]==4 or self.matrix[x,y]==6):
                    self.scoreWin += 1

    

    def XSizeCell(self):
        return self.width/25
    
    def YSizeCell(self):
        return self.height/25

    def Display(self, screen):
        for x in range(25):
            for y in range(25):
                if(self.matrix[y, x] == 1):
                    pygame.draw.rect(screen, (64, 128, 255), (self.XSizeCell()*x+0.5, self.YSizeCell()*y+0.5, self.XSizeCell()-0.5, self.YSizeCell()-0.5))
                elif(self.matrix[y, x] == 2):
                    pygame.draw.rect(screen, (0, 0, 0), (self.XSizeCell()*x, self.YSizeCell()*y, self.XSizeCell(), self.YSizeCell()))
                elif(self.matrix[y, x] == 6):
                    pygame.draw.circle(screen, (255, 0, 255), (self.XSizeCell()*(x+0.5), self.YSizeCell()*(y+0.5)), 5)
                elif(self.matrix[y, x] == 0 or self.matrix[y, x] == 4):
                    pygame.draw.circle(screen, (255, 0, 255), (self.XSizeCell()*(x+0.5), self.YSizeCell()*(y+0.5)), 1)