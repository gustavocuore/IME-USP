import math

def é_hipotenusa(x):
    i = 1
    j = 2
    soma = 0
    hipo = 0
    contador = 0
    while i <= x:
        while j <= x:
            if math.sqrt((i**2)+(j**2)) == x:
                contador = contador + 1
                teste = x
                if teste != hipo:
                    soma = soma + teste
                    hipo = teste
                j = j + 1
            j = j + 1
        i += 1
        j = 2
    i = 1

    if contador >= 1:
        return 1
    else:
        return 0

def soma_hipotenusas(n):
    soma = 0
    x = 1
    while x <= n:
        if é_hipotenusa(x) == 1:
            soma = soma + x
        x = x + 1
    return soma
