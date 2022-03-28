'''programa recebe 3 valores a, b, c e exibe as raízes de uma função quadrática
usar formula de bhaskara para imprimir as raízes
delta < 0 dizer que não tem raizes reais
delta == 0 dizer que só tem uma raíz real
delta > 0 dizer que tem duas raízes reais e apresentar

fórmula ax² + bx + c = 0
bhaskara = (-b +/- raiz(b² - 4ac)) / 2a
'''
import math

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta >= 0:
    if delta > 0:
        raiz_delta = math.sqrt(delta)
        raiz1 = (- b + raiz_delta) / (2 * a)
        raiz2 = (- b - raiz_delta) / (2 * a)
        print("A função tem duas raízes reais:")
        print("x1:",raiz1)
        print("x2:",raiz2)
    else:
        raiz1 = - b / (2 * a)
        print("A função tem apenas uma raíz real: ")
        print("x1:",raiz1)
else:
    print("Delta é negativo:",delta)
    print("Por isso, a função não tem raízes reais")