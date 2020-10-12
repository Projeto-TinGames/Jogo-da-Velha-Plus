import pygame
from pygame.locals import *

class Casa:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.rect = Rect((self.x,self.y), (self.width, self.height))

        self.valor = ''
        self.poderes = []
        self.bloquear = []

    def adiciona_poder(self,poder):
        self.poderes.append(poder)
        
def define_casas(tamanho,linhas,colunas):
    casas = []
    for l in range(linhas):
        casas.append([])
        for c in range(colunas):
            width = tamanho[0]//colunas
            height = tamanho[1]//linhas
            x = width*c
            y = height*l
            
            casas[l].append(Casa(x,y,width,height))

    return casas

