import pygame
import Scripts.class_casa as class_casa
from pygame.locals import *

class Tabuleiro:
    def __init__(self,quantidadeJogadores):
        self.tamanho = [600,600]
        self.quantidadeJogadores = quantidadeJogadores
        
        self.linhas = 4 + self.quantidadeJogadores - 2
        self.colunas = 4 + self.quantidadeJogadores - 2

        self.quantidadeCasas = self.linhas*self.colunas
        
        self.casas = class_casa.define_casas(self.tamanho,self.linhas,self.colunas)

    def desenha(self,tela):
        for c in range(1,len(self.casas[0])):
            pygame.draw.line(tela, (255, 255, 255), (c*self.casas[0][c].width, 0), (c*self.casas[0][c].width, self.tamanho[0]), 10)
        for l in range(1,len(self.casas)):
            pygame.draw.line(tela, (255, 255, 255), (0, l*self.casas[l][0].height), (self.tamanho[1], l*self.casas[l][0].height), 10)

    def posiciona_peca(self,tela,l,c,jogador):
        imgJogador = pygame.image.load("Imagens/"+jogador.valor+".png").convert_alpha()
        imgJogador = pygame.transform.scale(imgJogador, (self.casas[l][c].width//2, self.casas[l][c].height//2))
        tela.blit(imgJogador, (self.casas[l][c].x+self.casas[l][c].width//4, self.casas[l][c].y+self.casas[l][c].height//4))

        self.casas[l][c].valor = jogador #Altera o valor da casa para a string do jogador (X ou O)

        #Executa os poderes da casa
        for i in range(len(self.casas[l][c].poderes)):
            self.casas[l][c].poderes[i].executa_poder()

    def posiciona_poder(self,tela,l,c,jogador):
        #Desenha o poder posicionado
        imgPoder = pygame.image.load("Imagens/"+jogador.valor+".png").convert_alpha()
        imgPoder = pygame.transform.scale(imgPoder, (self.casas[l][c].width//2, self.casas[l][c].height//2))
        tela.blit(imgPoder, (self.casas[l][c].x+self.casas[l][c].width//4, self.casas[l][c].y+self.casas[l][c].height//4))

        #Coloca o poder na casa
        jogador.poderes[0].posiciona_poder(self.casas[l][c])
        self.casas[l][c].poderes.append(jogador.poderes[0])

quantidadeJogadores = int(input("Digite a quantidade de jogadores na partida: "))
instancia = Tabuleiro(quantidadeJogadores)
