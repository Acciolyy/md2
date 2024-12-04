x = int(input("Digite o número de termos da sequência de Fibonnaci: "))

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print(f"Sequência de Fibonacci até o {x}° termo:")
for i in range(1, x + 1):
    print(Fibonacci(i), end=" ")
print("")