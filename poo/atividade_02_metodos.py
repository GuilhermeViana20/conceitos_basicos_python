# atividade_02_metodos.py

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

# Teste
c1 = ContaBancaria("João")
c1.depositar(1000)
c1.sacar(500)
print(f"Saldo de {c1.titular}: R$ {c1.saldo}")
