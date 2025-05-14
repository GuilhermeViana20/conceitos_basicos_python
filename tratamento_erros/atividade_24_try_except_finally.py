try:
    arquivo = open("teste.txt", "r")
    print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    print("Finalizando execução.")