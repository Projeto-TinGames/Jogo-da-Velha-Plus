import pygame
from pygame.locals import *
from Scripts.variaveis_globais import jogadores
from Scripts.variaveis_globais import tabuleiro
from Scripts.variaveis_globais import turno
from Scripts.variaveis_globais import etapa
import Scripts.interface as interface

tela = pygame.display.set_mode((tabuleiro.tamanho[0]+200, tabuleiro.tamanho[1]), 0, 32)
pygame.display.set_caption("Jogo da Velha+")

poderesAtivados = []
cancelarPassarTurno = 0

print("")
print("---------Início da etapa: Batalha Naval---------")
print("")

def atualiza_tela():
    interface.desenha(tela,jogadores[turno],etapa,poderesAtivados)
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
        if (tabuleiro.casas[l][c].valor == '' and jogadores[turno].casasBloqueadas.count(tabuleiro.casas[l][c]) == 0):
            atualiza_jogoDaVelha(jogadores[turno],l,c)

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
            print("")
            print("---------Início da etapa: Jogo da Velha---------")
            print("")

def atualiza_jogoDaVelha(jogador,l,c):
    global turno,cancelarPassarTurno

    for i in range(len(jogadores)):
        if (tabuleiro.casas[l][c].valor == ''):
            jogadores[i].reduzir_casas_validas(tabuleiro.casas[l][c])
    
    tabuleiro.posiciona_peca(tela,l,c,jogador)
        
    #Testa vitória
    if (teste_vitoria(jogador)):
        print(jogador.valor + ' venceu')

    #Executa os poderes da casa
    while len(tabuleiro.casas[l][c].poderes) > 0:
        tabuleiro.casas[l][c].poderes[0].executa_poder(l,c)

    #Passa o turno
    if (cancelarPassarTurno == 0):
        turno += 1
        if (turno == len(jogadores)):
            turno = 0
    else:
        cancelarPassarTurno -= 1
    
    if (jogadores[turno].casasValidas <= 0):
        print("Empate")
        pygame.quit()
        exit()

def teste_vitoria(valor): #Testa as possibilidades de vitória
    return teste_horizontal(valor) or teste_vertical(valor) or teste_diagonal_colunas(valor) or teste_diagonal_linhas(valor)

def teste_horizontal(valor): #Pra cada linha ver o valor de cada coluna e comparar com o valor do jogador
    for l in range(len(tabuleiro.casas)):
        contador = 0
        casasVitoria = []
        for c in range(len(tabuleiro.casas[l])):
            if (tabuleiro.casas[l][c].valor == valor):
                contador += 1
                casasVitoria.append(tabuleiro.casas[l][c])
            else:
                contador = 0
                casasVitoria = []
            if (contador == 3):
                desenha_linha_vitoria(casasVitoria)
                return True

def teste_vertical(valor): #Pra cada coluna ver o valor de cada linha e comparar com o valor do jogado
    for c in range(len(tabuleiro.casas[0])):
        contador = 0
        casasVitoria = []
        for l in range(len(tabuleiro.casas)):
            if (tabuleiro.casas[l][c].valor == valor):
                contador += 1
                casasVitoria.append(tabuleiro.casas[l][c])
            else:
                contador = 0
                casasVitoria = []
            if (contador == 3):
                desenha_linha_vitoria(casasVitoria)
                return True 

def teste_diagonal_colunas(valor):
    for c in range(len(tabuleiro.casas[0])-2):
        contador = 0
        casasVitoria = []
        for l in range(len(tabuleiro.casas)):
            if (l+c < len(tabuleiro.casas[0])):
                if (tabuleiro.casas[l][l+c].valor == valor):
                    contador += 1
                    casasVitoria.append(tabuleiro.casas[l][l+c])
                else:
                    contador = 0
                    casasVitoria = []
                if (contador == 3):
                    desenha_linha_vitoria(casasVitoria)
                    return True
                
    for c in range(len(tabuleiro.casas[0])-2):
        contador = 0
        casasVitoria = []
        for l in range(len(tabuleiro.casas)):
            if (l+c < len(tabuleiro.casas[0])):
                if (tabuleiro.casas[l][len(tabuleiro.casas[0])-1-l-c].valor == valor):
                    contador += 1
                    casasVitoria.append(tabuleiro.casas[l][len(tabuleiro.casas[0])-1-l-c])
                else:
                    contador = 0
                    casasVitoria = []
                if (contador == 3):
                    desenha_linha_vitoria(casasVitoria)
                    return True

def teste_diagonal_linhas(valor):
    for l in range(len(tabuleiro.casas)-2):
        contador = 0
        casasVitoria = []
        for c in range(len(tabuleiro.casas[0])):
            if (l+c < len(tabuleiro.casas)):
                if (tabuleiro.casas[l+c][c].valor == valor):
                    contador += 1
                    casasVitoria.append(tabuleiro.casas[l+c][c])
                else:
                    contador = 0
                    casasVitoria = []
                if (contador == 3):
                    desenha_linha_vitoria(casasVitoria)
                    return True

    for l in range(len(tabuleiro.casas)-2):
        contador = 0
        casasVitoria = []
        for c in range(len(tabuleiro.casas[0])):
            if (l+c < len(tabuleiro.casas)):
                if (tabuleiro.casas[c+l][len(tabuleiro.casas[0])-1-c].valor == valor):
                    contador += 1
                    casasVitoria.append(tabuleiro.casas[c+l][len(tabuleiro.casas[0])-1-c])
                else:
                    contador = 0
                    casasVitoria = []
                if (contador == 3):
                    desenha_linha_vitoria(casasVitoria)
                    return True

def desenha_linha_vitoria(casasVitoria):
    primeiraCasaX = casasVitoria[0].x+casasVitoria[0].width//2
    primeiraCasaY = casasVitoria[0].y+casasVitoria[0].height//2
    posicaoPrimeiraCasa = [primeiraCasaX,primeiraCasaY]

    ultimaCasaX = casasVitoria[2].x+casasVitoria[2].width//2
    ultimaCasaY = casasVitoria[2].y+casasVitoria[2].height//2
    posicaoUltimaCasa = [ultimaCasaX,ultimaCasaY]
    
    pygame.draw.line(tela, (255, 255, 255), (posicaoPrimeiraCasa), (posicaoUltimaCasa), 10)
