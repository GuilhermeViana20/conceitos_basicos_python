# calculadora.py

def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "Erro: divisão por zero"

print("Calculadora Simples")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Escolha operação (+ - * /): ")

if op == "+":
    print("Resultado:", somar(a, b))
elif op == "-":
    print("Resultado:", subtrair(a, b))
elif op == "*":
    print("Resultado:", multiplicar(a, b))
elif op == "/":
    print("Resultado:", dividir(a, b))
else:
    print("Operação inválida.")
