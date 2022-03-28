b = int(input("digite a largura: "))
h = int(input("digite a altura: "))
x = 1
y = 1
    
while y <= h:
    espaco = b - 2
    if y == 1 or y == h:
        while x <= b:
            print("#", end = "")
            x += 1
        print()
    else:
        print("#"+espaco*" "+"#")
    y += 1
    x = 1