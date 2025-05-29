# AP2 - Gerenciador de Tarefas
tarefas_pendentes = []
tarefas_concluidas = []

def menu():
    print("\n====== AP2 ======")
    print("1. Adicionar tarefa")
    print("2. Editar tarefa")
    print("3. Apagar tarefa")
    print("4. Concluir tarefa")
    print("5. Ver tarefas")
    print("6. Sair")

def adicionar():
    descricao = input("Digite a descrição da tarefa: ")
    if not descricao:
        print("Descrição não pode ser vazia.")
        return
    try:
        relevancia = int(input("Digite a relevância (1 a 5): "))
        if relevancia < 1 or relevancia > 5:
            print("Relevância deve ser entre 1 e 5.")
            return
        tempo = int(input("Tempo estimado (minutos): "))
        if tempo <= 0:
            print("Tempo estimado inválido, ou menor que zero.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros para relevância e tempo.")
        return
    tarefas_pendentes.append({"descricao": descricao, "relevancia": relevancia, "tempo": tempo})
    print("Tarefa adicionada com sucesso!")

def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['descricao']} | Relevância: {t['relevancia']} | Tempo: {t['tempo']} min")

def editar():
    if not tarefas_pendentes:
        print("Sem tarefas pendentes.")
        return
    listar(tarefas_pendentes)
    try:
        i = int(input("Número da tarefa para editar: ")) - 1
        if i < 0 or i >= len(tarefas_pendentes):
            print("Número inválido.")
            return
        t = tarefas_pendentes[i]
        nova_desc = input("Nova descrição (ou Enter para manter): ").strip()
        if nova_desc:
            t["descricao"] = nova_desc
        nova_relev = input("Nova relevância (1 a 5 ou Enter): ").strip()
        if nova_relev:
            r = int(nova_relev)
            if 1 <= r <= 5:
                t["relevancia"] = r
        novo_tempo = input("Novo tempo (minutos ou Enter): ").strip()
        if novo_tempo:
            tempo = int(novo_tempo)
            if tempo > 0:
                t["tempo"] = tempo
        print("Tarefa editada.")
    except ValueError:
        print("Entrada inválida.")

def excluir():
    if not tarefas_pendentes:
        print("Sem tarefas pendentes.")
        return
    listar(tarefas_pendentes)
    try:
        i = int(input("Número da tarefa para excluir:")) - 1
        if 0 <= i < len(tarefas_pendentes):
            tarefas_pendentes.pop(i)
            print("Tarefa excluída.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def concluir():
    if not tarefas_pendentes:
        print("Sem tarefas pendentes.")
        return
    listar(tarefas_pendentes)
    try:
        i = int(input("Numero da tarefa para concluir: ")) - 1
        if 0 <= i < len(tarefas_pendentes):
            tarefa = tarefas_pendentes.pop(i)
            tarefas_concluidas.append(tarefa)
            print("Tarefa concluída.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def ver_tarefas():
    escolha = input("Ver (1) pendentes ou (2) concluídas: ")
    if escolha == '1':
        print("Tarefas pendentes:")
        listar(tarefas_pendentes)
    elif escolha == '2':
        print("Tarefas concluídas:")
        listar(tarefas_concluidas)
    else:
        print("Opção inválida.")

def iniciar():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar()
        elif opcao == '2':
            editar()
        elif opcao == '3':
            excluir()
        elif opcao == '4':
            concluir()
        elif opcao == '5':
            ver_tarefas()
        elif opcao == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

iniciar()