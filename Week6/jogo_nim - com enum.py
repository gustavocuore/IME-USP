'''
------------------- SEGREDO DO ENUNCIADO ------------------------
 computador_escolhe_jogada() e usuario_escolhe_jogada() || 20 A 40 LINHAS ||
 recebe dois parâmetros ( m,n )
 devem funcionar sozinhas (não precisa chamar outras funções do programa)
 não precisam de nenhum outro dado além de m,n
 devem devolver o número de peças removidas pela jogada (não vale devolver o número que sobrou no tabuleiro)
 não vale não devolver nada

 partida() função que pergunta os valores de m e n / decide quem começa o jogo / quem vai chamar as outras funções
 essa função terá um laço
 essa função pega o valor RETURN pelas funções e atualizar o valor de > n < de acordo
 identifica que o jogo acabou

 campeonato()
 só precisa chamar partida() três vezes (não precisa repetir nada)

 n,m não são globais

 pode criar uma função jogo() main() ou inicio() para começar o jogo

 checar se a entrada do usuario é valida podemos usar um laço de repetição (while true)
 verificar todos os casos inválidos (int, string, bool, float)

 ------------- REGRAS ---------------
 n peças inicialmente dispostas
 jogadores jogam alternadamente retirando uma ou m peças cada um
 quem tira as últimas peças possíveis ganha o jogo

 ----------- ESTRATÉGIA --------------
 sempre deixar múltiplos de m + 1
'''
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))
    while (escolha != 1) and (escolha != 2):
        escolha = int(input("2 - para jogar um campeonato "))

    print("")
    if escolha == 1:
        partida()
    if escolha == 2:
        print("Voce escolheu um campeonato!")
        print("")
        campeonato()

def usuario_escolhe_jogada(n,m):
    
    while (n > m) or (n < 1):
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        n = int(input("Quantas peças você vai tirar? "))
        print("")
    
    return n

def computador_escolhe_jogada(n,m):    
    i = m + 1
    if n % i != 0:
        while n % i !=0 and i > 0:
            n = n % i
            i = i - 1
        return i
    else:
        return i


def campeonato():
    u = 0
    c = 0
    x = 0
    print("**** Rodada 1 ****")
    print("")
    x = partida()
    if x == 2:
        c += 1
    else:
        u += 1
    print("")
    print("**** Rodada 2 ****")
    print("")

    x = partida()
    if x == 2:
        c += 1
    else:
        u += 1
    print("")
    print("**** Rodada 3 ****")
    print("")
    
    x = partida()
    if x == 2:
        c += 1
    else:
        u += 1
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você",u,"X",c,"Computador" )


def partida():
    n = int(input("Quantas peças? "))
    while (n <= 1):
        n = int(input("Quantas peças? "))

    m = int(input("Limite de peças por jogada? "))
    while (m < 1) or (m >= n):
        m = int(input("Limite de peças por jogada? "))
    print("")

    if (n % (m + 1)) == 0:
        print("Voce começa!")
        print("")
        tirar = int(input("Quantas peças você vai tirar? "))
        jogada_usuario = usuario_escolhe_jogada(tirar,m)
        n = n - jogada_usuario
        
        if jogada_usuario == 1:
            print("Você tirou uma peça.")
        else:
            print("Voce tirou",jogada_usuario,"peças.")
        
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam",n,"peças no tabuleiro.")

        usuario = 1
    else:
        print("Computador começa!")
        jogada_computador = computador_escolhe_jogada(n,m)
        n = n - jogada_computador
        print("")
        
        if jogada_computador == 1:
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou",jogada_computador,"peças.")

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam",n,"peças no tabuleiro.")

        usuario = 0
    
    while n > 0:
        if usuario == 1:
            print("")
            jogada_computador = computador_escolhe_jogada(n,m)
            n = n - jogada_computador

            if jogada_computador == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",jogada_computador,"peças.")

            if n >= 1:
                if n == 1 :
                    print("Agora resta apenas uma peça no tabuleiro.")
                else :
                    print("Agora restam",n,"peças no tabuleiro.")
            
            usuario = 0

        else:
            print("")
            tirar = int(input("Quantas peças você vai tirar? "))
            jogada_usuario = usuario_escolhe_jogada(tirar,m)
            n = n - jogada_usuario

            if jogada_usuario == 1:
                print("Você tirou uma peça.")
            else:
                print("Voce tirou",jogada_usuario,"peças.")
            
            if n >= 1:
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam",n,"peças no tabuleiro.")

            usuario = 1
    
    if usuario == 1:
        print("Fim do jogo! O usuário ganhou!")
        return 1

    else:
        print("Fim do jogo! O computador ganhou!")
        return 2
main()
