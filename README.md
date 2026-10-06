# Lista de Compras

Aplicação de terminal em Python para organizar uma lista de compras. Permite adicionar itens com quantidade, consultar a lista, marcar itens como comprados e removê-los.

## Requisitos

- Python 3

Não é necessário instalar dependências externas.

## Como executar

Na pasta raiz do projeto, execute:

```bash
python3 src/main.py
```

## Como usar

O programa apresenta um menu interativo:

1. **Adicionar item** — informa o nome e a quantidade. O nome não pode ficar vazio e a quantidade deve ser um número inteiro maior que zero.
2. **Listar itens** — mostra os itens numerados, suas quantidades e o status de compra.
3. **Marcar item como comprado** — informa o número do item na lista.
4. **Remover item** — informa o número do item a remover.
5. **Sair** — encerra o programa.

Os itens não ficam marcados como comprados ao serem adicionados; use a opção 3 para atualizar o status.

## Estrutura do projeto

```text
.
├── src/
│   ├── funcoes.py   # Operações da lista de compras
│   └── main.py      # Menu e ponto de entrada
└── lista_de_compras.ipynb
```

O notebook contém uma implementação independente para uso interativo. Para executar a aplicação pelo terminal, use `src/main.py`.

## Observação sobre os dados

Os itens são mantidos apenas na memória durante a execução. Ao sair do programa, a lista é apagada.
