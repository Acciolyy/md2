x = int(input("Digite um número inteiro positivo: "))

def soma(n):
    if n == 0:
        return 0
    return n + soma(n-1)

if x <= 0:
    print("Digite um número inteiro positivo.")
else:
    print(f"A soma dos números de 1 até {x} é {soma(x)}.")