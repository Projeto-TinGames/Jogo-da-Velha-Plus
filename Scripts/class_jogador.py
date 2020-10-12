from Scripts.class_poder import poderes
from Scripts.class_tabuleiro import instancia as tabuleiro
import random

#Classe para armazenar valores específicos dos jogadores
class Jogador:
    def __init__(self,valor):
        self.valor = valor
        self.casasValidas = tabuleiro.quantidadeCasas
        self.casasBloqueadas = []
        self.poderes = []
        for i in range(3):
            self.poderes.append(poderes[random.randint(0,1)])

    def reduzir_casas_validas(self,casa):
        if (self.casasBloqueadas.count(casa) == 0):
            self.casasValidas -= 1

    def colocar_poder(self,casa):
        print(str(type(self.poderes[0])) + " em " + str(type(casa)) + ".")
        self.poderes.pop(0)
        self.casasBloqueadas.append(casa)
        self.casasValidas -= 1

jogadoresPossiveis = [Jogador('X'),Jogador('O'),Jogador("Δ"),Jogador("[]")] #Os jogadores que estão na partida

jogadores = []

for i in range(tabuleiro.quantidadeJogadores):
    jogadores.append(jogadoresPossiveis[i])
