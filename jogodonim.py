def computador_escolhe_jogada(n, m):
    if n < m:
        pecas_computador = n
        return pecas_computador
    else:
        pecas_computador = m
        resto = 1
        while pecas_computador > 0 and resto != 0:
            n = n - pecas_computador
            resto = n % (m + 1)
            n = n + pecas_computador
            if resto == 0:
                return pecas_computador
            else:
                pecas_computador = pecas_computador - 1

        pecas_computador = m
        return pecas_computador

def usuario_escolhe_jogada (n, m):
    pecas_usuario = int(input("Quantas pecas deseja retirar? "))
    while pecas_usuario > n:
        print("Valor inválido. Só restam ", n," pecas.", m)
        pecas_usuario = int(input("Quantas peças voce quer retirar? "))  
    
    while pecas_usuario > m or pecas_usuario < 1:
        print("Você deve retirar no mínimo uma peça e no máximo ", m)
        pecas_usuario = int(input("Quantas peças voce quer retirar? "))
            
    return pecas_usuario

def partida():
    n = int(input("Quantas pecas estarão em jogo? "))
    m = int(input("Qual a quantidade maxima de pecas deve ser retirada por jogada? "))

    while m > n:
        print("m deve ser menor que n! Tente novamente.")
        n = int(input("Quantas pecas estarão em jogo? "))
        m = int(input("Qual a quantidade maxima de pecas a ser retirada por jogada? "))

    while n < 0 or m < 0:
        print("Oops! Escolha inválida! Tente de novo.")
        if n < 0:
            n = int(input("Quantas pecas estarão em jogo? "))
        if m < 0:
            m = int(input("Qual a quantidade maxima de pecas a ser retirada por jogada? "))

    mod = n % (m + 1)
    n_inicial = n

    while n != 0:
        if n == n_inicial:
            if mod == 0:
                print("Você começa!")
                jogada = 1
            else:
                print("O computador começa!")
                jogada = 0
        if jogada == 1:
            pecas_usuario = usuario_escolhe_jogada(n, m)
            n = n - pecas_usuario
            print("Usuario removeu ",pecas_usuario," pecas. Restam ", n, " pecas.")
            if n == 0:
                print("Você ganhou!")
                return jogada
            else:
                jogada = 0
        else:
            pecas_computador = computador_escolhe_jogada(n, m)
            n = n - pecas_computador
            print("Computador removeu ", pecas_computador, " pecas. Restam ", n, " pecas.")
            if n == 0:
                print("O computador ganhou!")
                return jogada
            else:
                jogada = 1
            
def campeonato():
    print("Você escolheu campeonato!")
    print("")
    usuario = 0
    computador = 0
    rodadas = 0
    
    while rodadas != 3:
        rodadas = rodadas + 1
        print("**** Rodada ", rodadas, " ****")
        vencedor = partida()
        if vencedor == 0:
            print("Fim do jogo! O computador ganhou!")
            computador = computador + 1
        else:
            print("Fim do jogo! Você ganhou!")
            usuario = usuario + 1

    print("**** Final do campeonato! ****")
    print("Placar: Você ", usuario," X ", computador," Computador")

    
print("Bem vindo ao Jogo do NIM! Escolha:" )
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
escolha = int(input(""))

while escolha != 1 and escolha != 2:
    escolha = int(input("Escolha inválida. Escolha 1 ou 2, para partida isolada ou campeonato:"))

if escolha == 1:
    escolha = partida()
if escolha == 2:
    escolha = campeonato()

