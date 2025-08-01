import sys

# Dados iniciais
usuarios = {"admin": "1234"}
produtos = {}
estoque = {}
pedidos = []
vendas = []

def login_inicial():
    print("=== Login Inicial ===")
    for _ in range(3):
        nome = input("Usuário: ")
        senha = input("Senha: ")
        if usuarios.get(nome) == senha:
            print(f"Bem-vindo, {nome}!")
            return True
        else:
            print("Usuário ou senha incorretos.")
    print("Tentativas excedidas. Encerrando o sistema.")
    sys.exit()

def cadastrar_usuario():
    nome = input("Novo nome de usuário: ")
    senha = input("Nova senha: ")
    if nome in usuarios:
        print("Usuário já existe.")
    else:
        usuarios[nome] = senha
        print("Usuário cadastrado com sucesso.")

def cadastrar_produto():
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade em estoque: "))
    produtos[codigo] = {"nome": nome, "preco": preco}
    estoque[codigo] = quantidade
    print("Produto cadastrado com sucesso.")

def registrar_pedido():
    codigo = input("Código do produto: ")
    if codigo in produtos:
        quantidade = int(input("Quantidade: "))
        if estoque[codigo] >= quantidade:
            total = produtos[codigo]["preco"] * quantidade
            pedidos.append({"codigo": codigo, "quantidade": quantidade, "total": total})
            estoque[codigo] -= quantidade
            vendas.append(total)
            print(f"Pedido registrado. Total: R${total:.2f}")
        else:
            print("Estoque insuficiente.")
    else:
        print("Produto não encontrado.")

def relatorio_vendas():
    print("\n=== Relatório de Vendas ===")
    print(f"Total de pedidos: {len(pedidos)}")
    print(f"Total arrecadado: R${sum(vendas):.2f}")
    print("Produtos vendidos:")
    for pedido in pedidos:
        nome = produtos[pedido["codigo"]]["nome"]
        print(f"- {nome}: {pedido['quantidade']} unidades")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar novo usuário")
        print("2. Cadastrar produto")
        print("3. Registrar pedido")
        print("4. Relatório de vendas")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            registrar_pedido()
        elif opcao == "4":
            relatorio_vendas()
        elif opcao == "5":
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida.")

# Início do sistema
if __name__ == "__main__":
    login_inicial()
    menu()
