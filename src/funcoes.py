# Lista de compras mantida em memória[cite: 1]
itens = []


def adicionar_item():
    """Adiciona um novo item à lista com validação de nome e quantidade[cite: 2]."""
    print("\n--- Adicionar Item ---")
    
    # Validação do nome (não pode ser vazio)[cite: 2]
    nome = input("Nome do item: ").strip()
    if not nome:
        print("Erro: O nome do item não pode ser vazio.")
        return

    # Validação da quantidade (deve ser um inteiro > 0)[cite: 2]
    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("Erro: A quantidade deve ser um inteiro maior que zero.")
            return
    except ValueError:
        print("Erro: Digite um número inteiro válido para a quantidade.")
        return

    # Estrutura do item conforme o modelo de dados[cite: 1]
    item = {
        "nome": nome,
        "quantidade": quantidade,
        "comprado": False  # Inicia como False[cite: 1]
    }
    
    itens.append(item)
    print(f"Item '{nome}' adicionado com sucesso!")


def listar_itens():
    """Exibe todos os itens da lista com seus respectivos índices e status[cite: 2]."""
    print("\n--- Lista de Compras ---")
    if not itens:
        print("A lista está vazia.")
        return

    for i, item in enumerate(itens, start=1):
        status = "[X]" if item["comprado"] else "[ ]"
        print(f"{i}. {status} {item['nome']} - Quantidade: {item['quantidade']}")


def marcar_comprado():
    """Marca um item da lista como comprado com base no número/índice[cite: 2]."""
    listar_itens()
    if not itens:
        return

    try:
        indice = int(input("\nDigite o número do item que deseja marcar como comprado: ")) - 1
        if 0 <= indice < len(itens):
            itens[indice]["comprado"] = True
            print(f"Item '{itens[indice]['nome']}' marcado como comprado!")
        else:
            print("Erro: Número de item inválido.")
    except ValueError:
        print("Erro: Digite um número inteiro válido.")


def remover_item():
    """Remove um item da lista com base no número/índice[cite: 2]."""
    listar_itens()
    if not itens:
        return

    try:
        indice = int(input("\nDigite o número do item que deseja remover: ")) - 1
        if 0 <= indice < len(itens):
            item_removido = itens.pop(indice)
            print(f"Item '{item_removido['nome']}' removido com sucesso!")
        else:
            print("Erro: Número de item inválido.")
    except ValueError:
        print("Erro: Digite um número inteiro válido.")