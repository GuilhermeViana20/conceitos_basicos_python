class IdadeInvalidaError(Exception):
    pass

def verificar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa.")
    print(f"Idade válida: {idade}")

try:
    idade = int(input("Digite sua idade: "))
    verificar_idade(idade)
except IdadeInvalidaError as e:
    print("Erro:", e)
except ValueError:
    print("Digite apenas números.")