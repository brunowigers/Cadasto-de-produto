def formatar_nome(nome):
    return nome.strip().title()


def cadastrar_produtos():
    nome = input("digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))  
    categoria = input("digite a categoria do produto: ")
    return (formatar_nome(nome), preco, categoria)

def salvar_produtos(produto):
    with open("produtos. txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[0]};{produto[1]};{produto[2]}\n"
        arquivo.write(linha)

def listar_produtos():
    try:
        with open("produtos. txc", "r", encoding="utf-8") as arquivo:
            for linha in arquivo: 
                nome, preco, categoria = linha.strip((";"))
                print(f"produto: {nome} | preço: R${preco} | categoria: {categoria} ")
    except FileNotFoundError:
        print("nenhum produto cadastrado ainda.")
while True:
    print("\n1 - cadastrar produtos")
    print("2 - listar produtos ")
    print("0 - sair")
    opcao = input("escolha:")

    if opcao == "1":
        produto = cadastrar_produtos()
        salvar_produtos(produto)
    elif opcao == "2":
        listar_produtos()
    elif opcao == "0":
        break
