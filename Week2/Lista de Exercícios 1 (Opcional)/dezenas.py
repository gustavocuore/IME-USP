numero = int(input("Digite um número inteiro: "))
dezena = ((numero % 1000) % 100) // 10
print("O dígito das dezenas é",dezena)