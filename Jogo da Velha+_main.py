import pygame
from pygame.locals import *
from sys import exit
import random

#Importando o gerenciador do jogo
import Scripts.game_manager as manager

pygame.init()                    

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()
        if e.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            manager.testa_pos(mouse_pos)

    manager.atualiza_tela()
            
    pygame.display.flip()
