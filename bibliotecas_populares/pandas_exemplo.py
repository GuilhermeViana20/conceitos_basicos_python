import pandas as pd

dados = {
    "Nome": ["Ana", "Carlos", "João"],
    "Idade": [25, 30, 22]
}

df = pd.DataFrame(dados)
print(df)
print("Média de idade:", df["Idade"].mean())