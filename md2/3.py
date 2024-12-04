x = int(input("Digite o número natural: "))

def rec(n):
    if n > x:
        return
    print(n)
    rec(n + 1)

if x < 1:
    print("Precisa que seja um número natural (maior ou igual a 1).")
else:
    rec(1)
