n = int(input("Insira um número inteiro: "))

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

while n > 0:
    if primaridade(n):
        print("primo")
    else:
        print("não primo")
    n = int(input("Insira um número inteiro: "))