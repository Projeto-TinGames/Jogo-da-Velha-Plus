import Scripts.game_manager as manager
import random

class Poder:
    def posiciona_poder(self,casa):
        self.casa = casa

    def executa_poder(self,l,c):
        manager.tabuleiro.casas[l][c].poderes.remove(self)
        print("Executar: " + str(self))

class Repeticao(Poder):
    def executa_poder(self,l,c):
        super().executa_poder(l,c)
        manager.turno -= 1
    
class Troca(Poder):
    def executa_poder(self,l,c):
        super().executa_poder(l,c)

        jogadores = manager.jogadores.copy()

        jogadoresMudar = manager.jogadores.copy()
        jogadoresMudarPara = manager.jogadores.copy()

        for i in range(len(jogadoresMudarPara)):
            while jogadoresMudar[i] == jogadoresMudarPara[i]:
                jogadoresMudarPara[i] = jogadores[random.randint(0,len(jogadores)-1)]
                
            jogadores.remove(jogadoresMudarPara[i])

        for i in range(len(jogadoresMudarPara)):
            print (jogadoresMudar[i].valor + " = " + jogadoresMudarPara[i].valor)

        for l in range(len(manager.tabuleiro.casas)):
            for c in range(len(manager.tabuleiro.casas[l])):
                if (manager.tabuleiro.casas[l][c].valor != ''):
                    indexMudar = jogadoresMudar.index(manager.tabuleiro.casas[l][c].valor)
                    
                    manager.atualiza_jogoDaVelha(jogadoresMudarPara[indexMudar],l,c)
                    manager.turno -= 1

class Remocao(Poder):
    def executa_poder(self,l,c):
        super().executa_poder(l,c)

        casasComValor = []
        posicoesCasasComValor = []

        for l in range(len(manager.tabuleiro.casas)):
            for c in range(len(manager.tabuleiro.casas[l])):
                if (manager.tabuleiro.casas[l][c].valor != manager.jogadores[manager.turno] and
                    manager.tabuleiro.casas[l][c].valor != ''):

                    casasComValor.append(manager.tabuleiro.casas[l][c])
                    posicoesCasasComValor.append([l,c])

        if (len(casasComValor) > 0):
            indexAleatoria = random.randint(0,len(casasComValor)-1)
            casaRemovida = casasComValor[indexAleatoria]
            casaRemovida.valor = ''
            manager.tabuleiro.remove_peca(manager.tela, posicoesCasasComValor[indexAleatoria][0], posicoesCasasComValor[indexAleatoria][1])
        
