def ePrimo(n):
    i = 1
    j = 1
    k = 0
    while i <= n:        
        while j <= i:
            resto = i % j
            if resto == 0:
                k += 1
            j += 1
        if k == 2:
            primo = i
            
        i = i + 1
        j = 1
        k = 0
    return primo

def maior_primo(x):
    if x > 1:
        return ePrimo(x)
