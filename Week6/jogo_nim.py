def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))
    while (escolha != 1) and (escolha != 2):
        escolha = int(input("2 - para jogar um campeonato "))
    print("")
    if escolha == 1:
        partida()
    if escolha == 2:
        print("Voce escolheu um campeonato!\n")
        campeonato()

def usuario_escolhe_jogada(n,m):
    tirar = 0
    while tirar == 0:
        tirar = int(input("Quantas peças você vai tirar? "))
        if (tirar > m) or (tirar < 1) or (tirar > n):
            print("\nOops! Jogada inválida! Tente de novo.\n")
            tirar = 0 
    return tirar

def computador_escolhe_jogada(n,m):    
    i = 1
    while i <= m:
        if (n - i) % (m + 1) == 0:
            return i
        i = i + 1
    return m   

def campeonato():
    u = 0
    c = 0
    x = 0
    print("**** Rodada 1 ****\n")
    x = partida()
    if x == 2:
        c += 1
    else:
        u += 1

    print("\n**** Rodada 2 ****\n")
    x = partida()
    if x == 2:
        c += 1
    else:
        u += 1
    
    print("\n**** Rodada 3 ****\n")
    x = partida()
    if x == 2:
        c += 1
    else:
        u += 1
    
    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você",u,"X",c,"Computador" )


def partida():
    n = int(input("Quantas peças? "))
    while (n < 1):
        n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while (m < 1):
        m = int(input("Limite de peças por jogada? "))
    print("")

    if (n % (m + 1) == 0):
        print("Voce começa!\n")
        jogada_usuario = usuario_escolhe_jogada(n,m)
        n = n - jogada_usuario        
        if jogada_usuario == 1:
            print("Você tirou uma peça.")
        else:
            print("Voce tirou",jogada_usuario,"peças.")        
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        if n > 1:
            print("Agora restam",n,"peças no tabuleiro.\n")
        usuario = 1
    else:
        print("Computador começa!\n")
        jogada_computador = computador_escolhe_jogada(n,m)
        n = n - jogada_computador        
        if jogada_computador == 1:
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou",jogada_computador,"peças.")
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        if n > 1:
            print("Agora restam",n,"peças no tabuleiro.\n")
        usuario = 0
    
    while n > 0:
        if usuario == 1:
            jogada_computador = computador_escolhe_jogada(n,m)
            n = n - jogada_computador
            if jogada_computador == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",jogada_computador,"peças.")

            if n >= 1:
                if n == 1 :
                    print("Agora resta apenas uma peça no tabuleiro.\n")
                else :
                    print("Agora restam",n,"peças no tabuleiro.\n")            
            usuario = 0
        else:
            jogada_usuario = usuario_escolhe_jogada(n,m)
            n = n - jogada_usuario

            if jogada_usuario == 1:
                print("\nVocê tirou uma peça.")
            else:
                print("Voce tirou",jogada_usuario,"peças.")
            
            if n >= 1:
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.\n")
                else:
                    print("Agora restam",n,"peças no tabuleiro.\n")
            usuario = 1
    
    if usuario == 1:
        print("Fim do jogo! O usuário ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 2
main()

input()
