class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criar dois objetos e imprimir os dados
p1 = Pessoa("Ana", 25)
p2 = Pessoa("Carlos", 30)

print(f"{p1.nome} tem {p1.idade} anos.")
print(f"{p2.nome} tem {p2.idade} anos.")
