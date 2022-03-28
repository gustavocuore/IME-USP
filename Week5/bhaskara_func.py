import math

def main():
    a = float(input("Insira o valor de a: "))
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))
    print(delta(a,b,c))
    imprime_raizes(a,b,c)

def delta(x,y,z):
    delta = y ** 2 - 4 * x * z
    return delta

def raiz1(x,y,z):
    return ((- y - math.sqrt(delta(x,y,z))) / (2 * x))

def raiz2(x,y,z):
    return ((- y + math.sqrt(delta(x,y,z))) / (2 * x))

def imprime_raizes(x,y,z):
    d = delta(x,y,z)
    if d >= 0:
        if d > 0:
            print("as raízes da equação são",raiz1(x,y,z),"e",raiz2(x,y,z))
        else:
            print("a raiz desta equação é",raiz1(x,y,z))
    else:
        print("esta equação não possui raízes reais")

main()