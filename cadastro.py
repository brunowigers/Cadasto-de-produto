def formatar_nome(nome):
    return nome.strip().title()
def cadastrar_produto():
    nome = input("digite o nome do produto:")
    preco = float("digite o preço do produto:")    
    categoria = input("digite a categoria do produto:")
    return (formatar_nome(nome), preco, categoria)
def salvar_produto(produto):
    with open("produtos. txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[0]};{produto[1]};{produto[2]}\n"
        arquivo.write(linha)
    def listar_produtos():
        try:
            with open("produtos. txc", "r", encoding="utl-8") as arquivo:
                for linha in arquivo: 
                    nome, preco, categoria = linha.strip((";"))
                    print(f"produto: {nome} ")