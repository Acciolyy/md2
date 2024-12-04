
x = int(input("Digite o número X: "))
y = int(input("Digite o número Y: "))


def mdc(x, y):
    while y != 0:
        r = x % y  
        x = y
        y = r
    return x


print(f"O MDC de {x} e {y} é {mdc(x, y)}")