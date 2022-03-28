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
        return 1
    else:
        return 0


def n_primos(n):
    k = 2
    primos = 0
    while k <= n:
        primos = primos + primaridade(k)
        k += 1
    return primos