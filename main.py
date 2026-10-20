
produtos = {}

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()

    if nome == "":
        print("Erro: o nome do produto é obrigatório.")
        return

    if nome in produtos:
        print("Esse produto já está cadastrado.")
        return

    try:
        quantidade = int(input("Quantidade em estoque: "))

        if quantidade < 0:
            print("Erro: a quantidade não pode ser negativa.")
            return

    except ValueError:
        print("Erro: digite uma quantidade inteira válida.")
        return

    produtos[nome] = quantidade
    print("Produto cadastrado com sucesso!")

def consultar_estoque():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- ESTOQUE ATUAL ---")

    for nome, quantidade in produtos.items():
        print(f"{nome}: {quantidade} unidade(s)")

while True:
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Consultar estoque")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        consultar_estoque()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
