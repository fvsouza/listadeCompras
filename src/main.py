from funcoes import (
    adicionar_item,
    listar_itens,
    marcar_comprado,
    remover_item
)


def main():
    """Menu principal interativo em loop[cite: 2, 3]."""
    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Listar itens")
        print("3. Marcar item como comprado")
        print("4. Remover item")
        print("5. Sair")
        
        opc = input("Escolha: ").strip()

        if opc == "1":
            adicionar_item()
        elif opc == "2":
            listar_itens()
        elif opc == "3":
            marcar_comprado()
        elif opc == "4":
            remover_item()
        elif opc == "5":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()