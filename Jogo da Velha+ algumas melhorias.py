# importando a bliblioteca do Python
import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

tamanho = [600,600]

quantidadeColunas = int(input("Digite a quantidade de colunas: "))
quantidadeLinhas = int(input("Digite a quantidade de linhas: "))

quantidadeCasas = quantidadeColunas*quantidadeLinhas

distanciaLinhasHorizontais = tamanho[0]//quantidadeColunas
distanciaLinhasVerticais = tamanho[1]//quantidadeLinhas

centroDaCasaX = distanciaLinhasHorizontais//2
centroDaCasaY = distanciaLinhasVerticais//2

tela = pygame.display.set_mode(tamanho, 0, 32)

pygame.display.set_caption("Jogo da Velha")

jogadores = ['X','O'] #Os jogadores que estão jogando a partida
turno = 0 #Variável de turno para controlar de quem dos jogadores no vetor é a vez
casasPreenchidas = 0 

#Classe para casas do tabuleiro
class Casa:
    def __init__(self,rect):
        self.rect = rect
        self.valor = ''
        self.poder = ''

#Cria uma matriz vazia para preencher com casas
casas = []
#Preenche a matriz com casas
for l in range(quantidadeLinhas):
    casas.append([None]*quantidadeColunas)
    for c in range(quantidadeColunas):
        rect = Rect((distanciaLinhasHorizontais*c, distanciaLinhasVerticais*l), (distanciaLinhasHorizontais, distanciaLinhasVerticais))
        casas[l][c] = Casa(rect)

def desenhar_tabuleiro():#Desenha o tabuleiro com base nas linhas e colunas do tabuleiro
                                                 
    for l in range(1,len(casas)):
        pygame.draw.line(tela, (255, 255, 255), (0, l*distanciaLinhasVerticais), (tamanho[1], l*distanciaLinhasVerticais), 10)
    for c in range(1,len(casas[0])):
        pygame.draw.line(tela, (255, 255, 255), (c*distanciaLinhasHorizontais, 0), (c*distanciaLinhasHorizontais, tamanho[0]), 10)

def testa_pos(mouse_pos,jogador):
    #Testa se a casa selecionada é válida
    global turno
    for l in range(len(casas)):
        for c in range(len(casas[l])):
            if (casas[l][c].rect.collidepoint(mouse_pos) and casas[l][c].valor == ''):
                atualiza_tabuleiro(jogador,casas[l][c],[centroDaCasaX+distanciaLinhasHorizontais*c,centroDaCasaY+distanciaLinhasVerticais*l])

def atualiza_tabuleiro(jogador,casa,pos):
    global jogadores,turno,quantidadeCasas,casasPreenchidas
    
    #Pega a imagem do jogador que jogou e desenha
    imgJogador = pygame.image.load(jogadores[turno]+".png").convert_alpha()
    imgJogador = pygame.transform.scale(imgJogador, (centroDaCasaX, centroDaCasaY))
    tela.blit(imgJogador, (pos[0] - centroDaCasaX//2, pos[1] - centroDaCasaY//2))
    
    casa.valor = jogador #Altera o valor da casa para a string do jogador (X ou O)
    
    casasPreenchidas += 1

    #Testa vitória ou empate
    if (teste_vitoria(jogadores[turno])):
        print(jogadores[turno] + ' venceu')
        pygame.quit()
        exit()
    elif (casasPreenchidas == quantidadeCasas):
        print("Empate")
        pygame.quit()
        exit()

    #Passa o turno
    turno += 1
    if (turno == len(jogadores)):
        turno = 0
    
def teste_vitoria(valor): #Testa as possibilidades de vitória
    return teste_horizontal(valor) or teste_vertical(valor) or teste_diagonal(valor)

def teste_horizontal(valor): #Pra cada linha ver o valor de cada coluna e comparar com o valor do jogador
    for l in range(len(casas)):
        contador = 0
        for c in range(len(casas[l])):
            if (casas[l][c].valor == valor):
                contador += 1
            else:
                contador = 0
            if (contador == 3):
                return True

def teste_vertical(valor): #Pra cada coluna ver o valor de cada linha e comparar com o valor do jogador
    for c in range(len(casas[0])):
        contador = 0
        for l in range(len(casas)):
            if (casas[l][c].valor == valor):
                contador += 1
            else:
                contador = 0
            if (contador == 3):
                return True 

def teste_diagonal(valor):
    contador = 0
    for c in range(len(casas[0])-2):
        for l in range(len(casas)):
            if (l+c < len(casas[0])):
                if (casas[l][l+c].valor == valor):
                    contador += 1
                else:
                    contador = 0
                if (contador == 3):
                    return True
                
    contador = 0
    for c in range(len(casas[0])-2):
        for l in range(len(casas)):
            if (l+c < len(casas[0])):
                if (casas[l][len(casas[0])-1-l-c].valor == valor):
                    contador += 1
                else:
                    contador = 0
                if (contador == 3):
                    return True 
        

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()
        if e.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            testa_pos(mouse_pos,jogadores[turno])

    desenhar_tabuleiro()
            
    pygame.display.flip()


            
            


