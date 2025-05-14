# lista_tarefas.py

def mostrar_tarefas():
    try:
        with open("tarefas.txt", "r") as f:
            tarefas = f.readlines()
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t.strip()}")
    except FileNotFoundError:
        print("Nenhuma tarefa ainda.")

def adicionar_tarefa(tarefa):
    with open("tarefas.txt", "a") as f:
        f.write(tarefa + "\n")

print("To-Do List")
while True:
    print("\n1. Ver tarefas\n2. Adicionar tarefa\n3. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        mostrar_tarefas()
    elif opcao == "2":
        tarefa = input("Nova tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == "3":
        break
