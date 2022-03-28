import math

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta >= 0:
    if delta > 0:
        raiz_delta = math.sqrt(delta)
        raiz1 = (- b - raiz_delta) / (2 * a)
        raiz2 = (- b + raiz_delta) / (2 * a)
        print("as raízes da equação são",raiz1,"e",raiz2)
    else:
        raiz1 = - b / (2 * a)
        print("a raiz desta equação é",raiz1)
else:
    print("esta equação não possui raízes reais")