
x = int(input("Digite o tamanho da tabela: "))


def criar_tabela_zn(x):
    t = []
    for i in range(x):
        l = []
        for j in range(x):
            valor = (i * j) % x
            l.append(valor)
        t.append(l)
    return t


def imprimir_tabela(t):
    for l in t:
        print(' '.join(map(str, l)))


t = criar_tabela_zn(x)


imprimir_tabela(t)