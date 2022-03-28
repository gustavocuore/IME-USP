n = int(input("Digite um número inteiro > 1: "))

fator = 2
multiplicidade = 0

def primaridade(x):
    i = 1
    cont = 0
    while i <= x:
        if x % i == 0:
            cont = cont + 1
            i = i + 1
        else:
            i = i + 1
    if cont == 2:
        return True
    else:
        return False

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print ("Fator ",fator, primaridade(fator), "multiplicidade = ", multiplicidade)
    fator = fator + 1
    multiplicidade = 0