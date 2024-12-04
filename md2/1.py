Var = int(input("Digite um número inteiro não negativo: "))

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)
if Var < 0:
   print("Fatorial não é definido para números negativos.\n") 
else:
    print(f"O fatorial de {Var} é {fatorial(Var)}")