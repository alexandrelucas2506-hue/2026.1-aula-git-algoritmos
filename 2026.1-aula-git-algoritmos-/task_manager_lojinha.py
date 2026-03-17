itens = []

while True:
    print("\n=== CARRINHO DA LOJINHA ===")
    print("1- Adicionar um item")
    print("2- Listar itens")
    print("3- Ver total do carrinho")
    print("4- Remover um item")
    print("5- Finalizar compra")
    print("6- Sair")
    print("==============================")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao not in ["1", "2", "3", "4", "5", "6"]:
        print("Opção Inválida!")
        continue
    
    if opcao == "1":
        print("\n=== PRODUTOS ===")
        print("1) Mouse Gamer - R$70.00")
        print("2) Teclado Gamer - R$160.00")
        print("3) Monitor - R$800.00")
        print("4) Mouse Ergonômico - R$100.00")
        print("5) Fita Led - R$30.00")
        print("6) Microfone - R$430.00")
        print("7) Adaptador P3 - R$10.00")
        print("===================")
        
        escolha = input("\nDigite o número do item: ")
        
        if escolha == "1":
            itens.append({"nome": "Mouse Gamer", "preco": 70.00})
            print(">> Mouse Gamer adicionado!")
        elif escolha == "2":
            itens.append({"nome": "Teclado Gamer", "preco": 160.00})
            print(">> Teclado Gamer adicionado!")
        elif escolha == "3":
            itens.append({"nome": "Monitor", "preco": 800.00})
            print(">> Monitor adicionado!")
        elif escolha == "4":
            itens.append({"nome": "Mouse Ergonômico", "preco": 100.00})
            print(">> Mouse Ergonômico adicionado!")
        elif escolha == "5":
            itens.append({"nome": "Fita Led", "preco": 30.00})
            print(">> Fita Led adicionada!")
        elif escolha == "6":
            itens.append({"nome": "Microfone", "preco": 430.00})
            print(">> Microfone adicionado!")
        elif escolha == "7":
            itens.append({"nome": "Adaptador P3", "preco": 10.00})
            print(">> Adaptador P3 adicionado!")
        else:
            print(">> Opção de produto inválida!")

    elif opcao == "2":
        if not itens:
            print("\nO carrinho está vazio!")
        else:
            print("\n=== SEU CARRINHO ===")
            for i, produto in enumerate(itens, 1):
                # Agora ele mostra o nome bonitinho
                print(f"{i}. {produto['nome']} - R${produto['preco']:.2f}")

    elif opcao == "3":
        # Para somar, pegamos apenas o 'preco' de cada dicionário na lista
        total = sum(p['preco'] for p in itens)
        print(f"\nTotal acumulado: R${total:.2f}")

    elif opcao == "4":
        if not itens:
            print("\nO carrinho está vazio! Não há o que remover.")
        else:
            # Primeiro, mostramos a lista para o usuário saber o que remover
            print("\n=== REMOVER ITEM SPECÍFICO ===")
            for i, produto in enumerate(itens, 1):
                print(f"{i}. {produto['nome']}")
            
            try:
                indice_str = input("\nDigite o número do item que deseja remover (ou '0' para cancelar): ")
                indice = int(indice_str)
                
                if indice == 0:
                    print("Operação cancelada.")
                elif 1 <= indice <= len(itens):
                    # Removemos usando o índice (ajustado para -1 porque a lista começa em 0)
                    removido = itens.pop(indice - 1)
                    print(f">> Sucesso! {removido['nome']} foi removido do carrinho.")
                else:
                    print("Número inválido! Esse item não existe na lista.")
            except ValueError:
                print("Erro: Por favor, digite apenas números!")

    elif opcao == "5":
        if itens:
            total = sum(p['preco'] for p in itens)
            print(f"\n=== COMPRA FINALIZADA ===")
            print(f"Total pago: R${total:.2f}")
            itens.clear()
            print("Obrigado! Volte sempre.")
        else:
            print("Adicione algo ao carrinho primeiro!")

    elif opcao == "6":
        print("Até logo!")
        break