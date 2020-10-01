# importando a bliblioteca do Python
import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

#Pede a quantidade de colunas e linhas do tabuleiro e calcula o número de casas (apenas conceitual, então coloco automaticamente em 3x3)
quantidadeColunas = int(input("Digite a quantidade de colunas: "))
quantidadeLinhas = int(input("Digite a quantidade de linhas: "))
quantidadeColunas = 3
quantidadeLinhas = 3
quantidadeCasas = quantidadeColunas*quantidadeLinhas

tela = pygame.display.set_mode((600, 600), 0, 32)

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
        rect = Rect((200*c, 200*l), (200, 200))
        casas[l][c] = Casa(rect)

def desenhar_tabuleiro():
    #Desenha o tabuleiro com base nas linhas e colunas do tabuleiro
    for l in range(1,len(casas)):
        pygame.draw.line(tela, (255, 255, 255), (0, l*200), (600, l*200), 10)
    for c in range(1,len(casas[l])):
        pygame.draw.line(tela, (255, 255, 255), (c*200, 0), (c*200, 600), 10)

def testa_pos(mouse_pos,jogador):
    #Testa se a casa selecionada é válida
    global turno
    for l in range(len(casas)):
        for c in range(len(casas[l])):
            if (casas[l][c].rect.collidepoint(mouse_pos) and casas[l][c].valor == ''):
                atualiza_tabuleiro(jogador,casas[l][c],[100+200*c,100+200*l])

def atualiza_tabuleiro(jogador,casa,pos):
    global jogadores,turno,quantidadeCasas,casasPreenchidas
    
    #Pega a imagem do jogador que jogou e desenha
    imgJogador = pygame.image.load(jogadores[turno]+".png").convert_alpha()
    imgJogador = pygame.transform.scale(imgJogador, (100, 100))
    tela.blit(imgJogador, (pos[0] - 50, pos[1] - 50))
    
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
    
def teste_vitoria(valor): #Testa as possibilidades de vitória (precisa de algumas mudanças, mas essa é a lógica)
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

def teste_diagonal(valor): #Precisa de melhorias, mas funciona em 3x3
    contador = 0
    for l in range(len(casas)):
        if (casas[l][l].valor == valor):
            contador += 1
        else:
            contador = 0
        if (contador == 3):
            return True 

    contador = 0
    for l in range(len(casas)):
        if (casas[l][len(casas)-l-1].valor == valor):
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


            
            


