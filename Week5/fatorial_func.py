print("Para n >= k insira:")
n = int(input("Valor de n: "))
k = int(input("Valor de k: "))

def fatorial(x):
    fat = 1
    i = 1
    if x >= 0:
        if x > 0:
            while i <= x:
                fat = fat * i
                i += 1
            return fat

        else: 
            return fat


def binomial():
    binomial = int(fatorial(n) / (fatorial(k) * fatorial(n-k)))
    print(binomial)


binomial()
