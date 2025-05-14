# atividade_03_heranca.py

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

# Teste
dog = Cachorro("Rex")
cat = Gato("Luna")
dog.emitir_som()
cat.emitir_som()