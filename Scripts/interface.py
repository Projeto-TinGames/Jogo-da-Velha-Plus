import pygame

def desenha(tela,jogador,etapa,poderesAtivados): #Desenha UI
    tela.blit(pygame.Surface([200,600]),[600,0])
    desenhaTurno(tela,jogador)
    desenhaPoderes(tela,jogador,etapa,poderesAtivados)

def desenhaTurno(tela,jogador):
    desenhaEmptyRect(tela,652,38,100,100)
    imgJogador = pygame.image.load("Imagens/"+jogador.valor+".png").convert_alpha()
    imgJogador = pygame.transform.scale(imgJogador, (75, 75))
    tela.blit(imgJogador, (665, 50))

def desenhaPoderes(tela,jogador,etapa,poderesAtivados):
    for i in range(3):
        desenhaEmptyRect(tela,652,140 + 110*(i+1)-12,100,100)
    
    if etapa == 'Batalha Naval': 
        for i in range(len(jogador.poderes)):
            imgJogador = pygame.image.load("Imagens/"+jogador.valor+".png").convert_alpha()
            imgJogador = pygame.transform.scale(imgJogador, (75, 75))
            tela.blit(imgJogador, (665, 140 + 110*(i+1)))
            
    else:
        for i in range(len(poderesAtivados)):
            imgJogador = pygame.image.load("Imagens/"+jogador.valor+".png").convert_alpha()
            imgJogador = pygame.transform.scale(imgJogador, (75, 75))
            tela.blit(imgJogador, (665, 140 + 110*(i+1)))

def desenhaEmptyRect(tela,x,y,width,height):
    pygame.draw.rect(tela,[255,255,255],(x,y,width,height))
    pygame.draw.rect(tela,[0,0,0],(x+5,y+5,width-10,height-10))
        
