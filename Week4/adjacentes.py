numero = int(input("Digite um número: "))

adjacente = False
nadjacente = 0

while numero % 10 != 0:
    ultdigito = numero % 10
    x = ultdigito
    numero = numero // 10
    ultdigito = numero % 10
    y = ultdigito
    if x == y:
        adjacente = True
        nadjacente = nadjacente + 1

if nadjacente > 0:
    print("Possui adjacente")
else:
    print("Não possui nenhum adjacente.")