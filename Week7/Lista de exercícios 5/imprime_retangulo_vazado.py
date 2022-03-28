b = int(input("digite a largura: "))
h = int(input("digite a altura: "))
x = 1
y = 1
    
if h <= 2:
    while y <= h:
        while x <= b:
            print("#",end = "")
            x += 1
        y += 1
        x = 1
        print()
else:
    while x <= b:
        print("#", end = "")
        x += 1
    print()
    x = 1
    while y <= (h-2):
        espaco = b - 2
        print("#"+espaco*" "+"#")
        y += 1
    x = 1
    while x <= b:
        print("#", end = "")
        x += 1
