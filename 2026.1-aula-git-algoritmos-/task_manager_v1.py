# Armazenar tarefas (por enquanto em memória)
tarefas = []

# Loop infinito até o usuário escolher sair
while True:
    # Exibir Menu
    print("\n=== TASK MANAGER v1.0 ===")
    print("1 - Criar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Contar Tarefas")
    print("4 - Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    # Validar entrada
    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida! Digite 1, 2, 3 ou 4")
        continue
    # Processar Opção
    if opcao == "1":
        # Subfunção: Criar tarefa
        nome = input("Nome da tarefa: ")
        if nome.strip(): #Validar que não está vazio
            tarefas.append(nome)
            print(f"Tarefa '{nome}' criada com sucesso!")
        else:
            print("Nome da tarefa não pode ser vazio!")
            
    elif opcao == "2":
        # Subfunção listar tarefas
        if len(tarefas) == 0:
            print("Nenhuma tarefa registrada ainda")
        else: print ("\nSuas tarefas:")
        for i, tarefa in enumerate (tarefas, 1):
            print(f" {i}. {tarefa}")
            
    elif opcao == "3":
        # Ao listar, mostrar: "Você tem 3 tarefas"
        print(f"Você tem {len(tarefas)} tarefa(s)")
        
    elif opcao =="4":
        #Subfunção Sair
        print("Até Logo!")
        break