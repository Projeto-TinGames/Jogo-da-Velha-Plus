import Scripts.game_manager as manager
import random

class Poder:
    def posiciona_poder(self,casa):
        self.casa = casa

    def executa_poder(self,l,c):
        manager.tabuleiro.casas[l][c].poderes.remove(self)
        if (len(manager.poderesAtivados) == 3):
            del manager.poderesAtivados[0]
        manager.poderesAtivados.append(self)
        print("Executar: " + str(self))

class Repeticao(Poder):
    def executa_poder(self,l,c):
        super().executa_poder(l,c)
        manager.cancelarPassarTurno += 1
    
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

        manager.cancelarTesteVitoria = True

        for l in range(len(manager.tabuleiro.casas)):
            for c in range(len(manager.tabuleiro.casas[l])):
                if (manager.tabuleiro.casas[l][c].valor != ''):
                    indexMudar = jogadoresMudar.index(manager.tabuleiro.casas[l][c].valor)
                    
                    manager.atualiza_jogoDaVelha(jogadoresMudarPara[indexMudar],l,c)
                    manager.turno -= 1

        manager.cancelarTesteVitoria = False

        for jogador in manager.jogadores:
            manager.teste_vitoria(jogador)

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

class Pular_Vez(Poder):
    def executa_poder(self,l,c):
        super().executa_poder(l,c)
        
        manager.turno += 1
        if (manager.turno == len(manager.jogadores)):
            manager.turno = 0

class Inverter_Ordem(Poder):
    def executa_poder(self,l,c):
        super().executa_poder(l,c)

        jogador = manager.jogadores[manager.turno]
        
        manager.jogadores.reverse()
        manager.turno = manager.jogadores.index(jogador)

class Voltar_Turno(Poder):
    def executa_poder(self,l,c):
        super().executa_poder(l,c)

        manager.cancelarPassarTurno = 1

        manager.turno -= 1
