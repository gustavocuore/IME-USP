n = int(input("Digite um número inteiro: "))
i = 1
k = 0
if n > 0:
    while i <= n:
        r = n % i
        if r == 0:
            k += 1
        i += 1        
if k > 2 or n == 0:
    print("nao primo")
else:
    print("primo")