def maior_elemento(lista):
    x = lista[0]
    maior = x
    for numero in lista:
        y = numero
        if y >= x and y >= maior:
            maior = y
        x = numero
    return maior

