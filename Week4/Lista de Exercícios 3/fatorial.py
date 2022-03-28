n = int(input("Digite o valor de n: "))
fat = 1
i = 1
if n >= 0:
    if n > 0:
        while i <= n:
            fat = fat * i
            i += 1
        print(fat)

    else: 
        print(fat)
