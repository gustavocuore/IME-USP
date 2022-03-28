b = int(input("digite a largura: "))
h = int(input("digite a altura: "))

x = 1
y = 1
while y <= h:
    while x <= b:
        print("#",end = "")
        x += 1
    y += 1
    x = 1
    print()
