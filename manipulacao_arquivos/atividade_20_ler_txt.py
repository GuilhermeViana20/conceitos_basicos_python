# atividade_02_ler_txt.py

with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
