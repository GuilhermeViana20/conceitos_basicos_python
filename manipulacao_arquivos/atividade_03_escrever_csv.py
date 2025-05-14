# atividade_03_escrever_csv.py

import csv

with open("usuarios.csv", "w", newline="") as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(["Nome", "Idade"])
    escritor.writerow(["Ana", 25])
    escritor.writerow(["Carlos", 30])
