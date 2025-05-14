import csv

with open("usuarios.csv", "r") as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)
