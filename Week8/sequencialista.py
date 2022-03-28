n = int(input("Digite um número inteiro terminado por 0: "))
sequencia = []
while n != 0:
    sequencia.append(n)
    n = int(input("Digite um número inteiro terminado por 0: "))

j = len(sequencia)
j = -1 * j
i = -1
while i >= j:
    print(sequencia[i], end = " ")
    i = i - 1