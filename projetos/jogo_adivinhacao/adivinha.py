# adivinha.py

import random

numero_secreto = random.randint(1, 10)
tentativas = 3

print("Jogo de Adivinhação – Tente adivinhar o número de 1 a 10")

for _ in range(tentativas):
    palpite = int(input("Seu palpite: "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
else:
    print(f"Você perdeu! O número era {numero_secreto}.")
