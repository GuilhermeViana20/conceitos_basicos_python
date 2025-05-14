import tkinter as tk

def saudacao():
    nome = entrada.get()
    label_resultado["text"] = f"Olá, {nome}!"

janela = tk.Tk()
janela.title("Saudação")

tk.Label(janela, text="Digite seu nome:").pack()
entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Saudar", command=saudacao).pack()
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()