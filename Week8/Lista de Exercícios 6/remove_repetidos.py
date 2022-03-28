def remove_repetidos(lista):
    lista_limpa = []
    for numero in lista:
        if (numero not in lista_limpa):
            lista_limpa.append(numero)
    lista_ordenada = sorted(lista_limpa)

    return(lista_ordenada)
