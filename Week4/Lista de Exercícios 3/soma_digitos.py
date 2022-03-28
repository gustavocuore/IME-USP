n = int(input("Digite um número inteiro: "))
soma = 0
while n > 0:
    while n % 10 !=0:
        udigit = n % 10
        soma = soma + udigit
        n = n // 10
    n = n // 10
print(soma)
