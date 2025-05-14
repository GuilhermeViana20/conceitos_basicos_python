try:
    num = int(input("Digite um número: "))
    resultado = 10 / num
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: divisão por zero.")
except ValueError:
    print("Erro: valor inválido.")