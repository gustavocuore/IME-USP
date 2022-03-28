n = int(input("Digite um número inteiro: "))
n_adjacente = 0
z = 0
while n > 0:
    if n % 10 !=0:
        z = 0
        udigit = n % 10
        x = udigit
        n = n // 10
        udigit = n % 10
        y = udigit
        if x == y:
            n_adjacente += 1
    else: 
        z += 1
        n = n // 10
        if z > 1:
            n_adjacente += 1
    
if n_adjacente > 0:
    print("sim")
else:
    print("não")