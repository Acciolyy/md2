x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

def mdc(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

def mmc(x, y):
    return x * y // mdc(x, y)

print(f"O MMC de {x} e {y} é {mmc(x, y)}")