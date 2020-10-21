import Scripts.game_manager as manager
import random

class Poder:
    def posiciona_poder(self,casa):
        self.casa = casa

    def executa_poder(self,l,c):
        manager.tabuleiro.casas[l][c].poderes.remove(self)
        print("Executar: " + str(self))

class Velocidade(Poder):
    def executa_poder(self,l,c):
        super().executa_poder(l,c)
        manager.turno -= 1
    
class Troca(Poder):
    def executa_poder(self,l,c):
        super().executa_poder(l,c)

        jogadoresMudar = manager.jogadores.copy()
        jogadoresMudarPara = manager.jogadores.copy()

        for i in range(len(jogadoresMudarPara)):
            while jogadoresMudar[i] == jogadoresMudarPara[i]:
                jogadoresMudarPara[i] = jogadoresMudar[random.randint(0,len(jogadoresMudar)-1)]

        for l in range(len(manager.tabuleiro.casas)):
            for c in range(len(manager.tabuleiro.casas[l])):
                if (manager.tabuleiro.casas[l][c].valor != ''):
                    indexMudar = jogadoresMudar.index(manager.tabuleiro.casas[l][c].valor)
                    
                    manager.atualiza_jogoDaVelha(jogadoresMudarPara[indexMudar],l,c)
                    manager.turno -= 1
