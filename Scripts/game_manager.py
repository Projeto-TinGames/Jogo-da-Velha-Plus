import pygame
from pygame.locals import *
from Scripts.class_jogador import jogadores
from Scripts.class_tabuleiro import instancia as tabuleiro

tela = pygame.display.set_mode(tabuleiro.tamanho, 0, 32)
pygame.display.set_caption("Jogo da Velha+")

etapa = "Batalha Naval"
turno = 0

def atualiza_tela():
    tabuleiro.desenha(tela)

def testa_pos(mouse_pos): #Testa se a casa selecionada é válida
    for l in range(len(tabuleiro.casas)):
        for c in range(len(tabuleiro.casas[l])):
            if (tabuleiro.casas[l][c].rect.collidepoint(mouse_pos)):
                atualiza_jogo(l,c)

def atualiza_jogo(l,c):
    if (etapa == "Batalha Naval"):
        atualiza_batalhaNaval(l,c)
    else:
        atualiza_jogoDaVelha(l,c)

def atualiza_batalhaNaval(l,c):
    global turno, etapa

    tabuleiro.posiciona_poder(tela,l,c,jogadores[turno])

    #Remove o poder posicionado do vetor de poderes
    jogadores[turno].colocar_poder(tabuleiro.casas[l][c])

    #Passa o turno na batalha naval
    if (len(jogadores[turno].poderes) == 0):
        tela.blit(pygame.Surface([600,600]),[0,0])
        turno += 1
        if (turno == len(jogadores)):
            turno = 0
            etapa = "Jogo da Velha"

def atualiza_jogoDaVelha(l,c):
    global turno
    
    if (tabuleiro.casas[l][c].valor == '' and jogadores[turno].casasBloqueadas.count(tabuleiro.casas[l][c]) == 0):
        tabuleiro.posiciona_peca(tela,l,c,jogadores[turno])

        for i in range(len(jogadores)):
            jogadores[i].reduzir_casas_validas(tabuleiro.casas[l][c])
        
        #Testa vitória ou empate
        if (teste_vitoria(jogadores[turno])):
            print(jogadores[turno].valor + ' venceu')
            pygame.quit()
            exit()

        #Passa o turno
        turno += 1
        if (turno == len(jogadores)):
            turno = 0

        if (jogadores[turno].casasValidas <= 0):
            print("Empate")
            pygame.quit()
            exit()

def teste_vitoria(valor): #Testa as possibilidades de vitória
    return teste_horizontal(valor) or teste_vertical(valor) or teste_diagonal_colunas(valor) or teste_diagonal_linhas(valor)

def teste_horizontal(valor): #Pra cada linha ver o valor de cada coluna e comparar com o valor do jogador
    for l in range(len(tabuleiro.casas)):
        contador = 0
        for c in range(len(tabuleiro.casas[l])):
            if (tabuleiro.casas[l][c].valor == valor):
                contador += 1
            else:
                contador = 0
            if (contador == 3):
                return True

def teste_vertical(valor): #Pra cada coluna ver o valor de cada linha e comparar com o valor do jogador
    for c in range(len(tabuleiro.casas[0])):
        contador = 0
        for l in range(len(tabuleiro.casas)):
            if (tabuleiro.casas[l][c].valor == valor):
                contador += 1
            else:
                contador = 0
            if (contador == 3):
                return True 

def teste_diagonal_colunas(valor):
    contador = 0
    for c in range(len(tabuleiro.casas[0])-2):
        for l in range(len(tabuleiro.casas)):
            if (l+c < len(tabuleiro.casas[0])):
                if (tabuleiro.casas[l][l+c].valor == valor):
                    contador += 1
                else:
                    contador = 0
                if (contador == 3):
                    return True
                
    contador = 0
    for c in range(len(tabuleiro.casas[0])-2):
        for l in range(len(tabuleiro.casas)):
            if (l+c < len(tabuleiro.casas[0])):
                if (tabuleiro.casas[l][len(tabuleiro.casas[0])-1-l-c].valor == valor):
                    contador += 1
                else:
                    contador = 0
                if (contador == 3):
                    return True

def teste_diagonal_linhas(valor):
    contador = 0
    for l in range(len(tabuleiro.casas)-2):
        for c in range(len(tabuleiro.casas[0])):
            if (l+c < len(tabuleiro.casas)):
                if (tabuleiro.casas[l+c][c].valor == valor):
                    contador += 1
                else:
                    contador = 0
                if (contador == 3):
                    return True

    contador = 0
    for l in range(len(tabuleiro.casas)-2):
        for c in range(len(tabuleiro.casas[0])):
            if (l+c < len(tabuleiro.casas)):
                if (tabuleiro.casas[c+l][len(tabuleiro.casas[0])-1-c].valor == valor):
                    contador += 1
                else:
                    contador = 0
                if (contador == 3):
                    return True
