#fazer um programa que o usuário digite um número e cada vez que ele digitar, o programa retorna o fatorial dele

n = int(input("Insira um número inteiro positivo: "))
while n >= 0:
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    print(fat)
    n = int(input("Insira um número inteiro: "))
