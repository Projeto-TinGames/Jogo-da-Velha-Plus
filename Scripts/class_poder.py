class Poder:
    def posiciona_poder(self,casa):
        self.casa = casa

    def executa_poder(self):
        print("Executar: " + str(self))

class Velocidade(Poder):
    pass

class Inversao(Poder):
    pass

poderes = [Velocidade(),Inversao()]
