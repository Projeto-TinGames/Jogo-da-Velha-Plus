turno = 0
etapa = "Batalha Naval"

poderes = []
tabuleiro = ''
jogadores = []

def define_poderes():
    import Scripts.class_poder as class_poder
    global poderes
    poderes = [class_poder.Repeticao(),class_poder.Troca(),
               class_poder.Remocao(),class_poder.Pular_Vez(),
               class_poder.Inverter_Ordem(),class_poder.Voltar_Turno()]

def define_tabuleiro():
    import Scripts.class_tabuleiro as class_tabuleiro
    global tabuleiro
    quantidadeJogadores = int(input("Digite a quantidade de jogadores na partida: "))
    tabuleiro = class_tabuleiro.Tabuleiro(quantidadeJogadores)
    
def define_jogadores():
    import Scripts.class_jogador as class_jogador
    global jogadores, tabuleiro, poderes
    jogadoresPossiveis = [class_jogador.Jogador('X', tabuleiro, poderes),
                          class_jogador.Jogador('O', tabuleiro, poderes),
                          class_jogador.Jogador("Δ", tabuleiro, poderes),
                          class_jogador.Jogador("[]", tabuleiro, poderes)]

    #Os jogadores que estão na partida
    for i in range(tabuleiro.quantidadeJogadores):
        jogadores.append(jogadoresPossiveis[i])

define_poderes()
define_tabuleiro()
define_jogadores()
    
