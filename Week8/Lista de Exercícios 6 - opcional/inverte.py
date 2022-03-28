n = int(input("Digite um número: "))
sequencia = []
while n != 0:
    sequencia.append(n)
    n = int(input("Digite um número: "))

j = len(sequencia)
j = -1 * j
i = -1
while i >= j:
    print(sequencia[i], end = "\n")
    i = i - 1