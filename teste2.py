import os
import time
import pandas as pd

# Arquivos Excel
ARQ_CLIENTES = "clientes.xlsx"
ARQ_PRODUTOS = "produtos.xlsx"
ARQ_PEDIDOS = "pedidos.xlsx"

# Carregar dados ou inicializar
def carregar_dados():
    if os.path.exists(ARQ_CLIENTES):
        clientes = pd.read_excel(ARQ_CLIENTES, engine='openpyxl').to_dict(orient='records')
    else:
        clientes = []

    if os.path.exists(ARQ_PRODUTOS):
        produtos = pd.read_excel(ARQ_PRODUTOS, engine='openpyxl').values.tolist()
    else:
        produtos = [['1', 'café preto', 3], ['2', 'café expresso', 5]]

    if os.path.exists(ARQ_PEDIDOS):
        pedidos = pd.read_excel(ARQ_PEDIDOS, engine='openpyxl').to_dict(orient='records')
    else:
        pedidos = []

    return clientes, produtos, pedidos

# Salvar dados
def salvar_dados():
    pd.DataFrame(clientes).to_excel(ARQ_CLIENTES, index=False)
    pd.DataFrame(produtos, columns=["codigo", "nome", "preco"]).to_excel(ARQ_PRODUTOS, index=False)
    pedidos_expandidos = []
    for p in pedidos:
        for item in p["itens"]:
            pedidos_expandidos.append({
                "id": p["id"],
                "cliente": p["cliente"],
                "codigo": item["codigo"],
                "nome": item["nome"],
                "quantidade": item["quantidade"],
                "preco": item["preco"]
            })
    pd.DataFrame(pedidos_expandidos).to_excel(ARQ_PEDIDOS, index=False)

# Dados iniciais
logins = [('admin', '1234'), ('Samuel', '1234')]
clientes, produtos, pedidos = carregar_dados()
proximo_id = max([p["id"] for p in pedidos], default=0) + 1

# Utilitários
def logo():
    print('-'*33)
    print('='*5, 'COFFEE SHOPS TIA ROSA', '='*5)
    print('-'*33)

def menu():
    print("-" * 30)
    print('1 - Pedido\n2 - Cadastro Cliente\n3 - Produtos\n4 - Sair') 

def sai(): 
    print("\nEncerrando", end="")
    for _ in range(5):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print('\n')
    print('-'*33)
    print('='*5, 'COFFEE SHOPS TIA ROSA', '='*5)
    print('-'*33)
    salvar_dados()
    quit()

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# CRUD Produtos
def mostrar_produtos():
    print("\nCódigo".ljust(10) + "Produto".ljust(20) + "Preço (R$)")
    print("-" * 40)
    for codigo, nome, preco in produtos:
        print(codigo.ljust(10) + nome.ljust(20) + f"R$ {preco:.2f}")
    print("-" * 40)

def adicionar_produto():
    codigo = input("Código: ")
    if any(p[0] == codigo for p in produtos):
        print("Código já existente.")
        return
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    produtos.append([codigo, nome, preco])
    print("Produto adicionado com sucesso!")

def atualizar_produto():
    codigo = input("Digite o código do produto a atualizar: ")
    for produto in produtos:
        if produto[0] == codigo:
            produto[1] = input("Novo nome: ")
            produto[2] = float(input("Novo preço: "))
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def deletar_produto():
    codigo = input("Digite o código do produto a deletar: ")
    for produto in produtos:
        if produto[0] == codigo:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")

# CRUD Clientes
def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    clientes.append({"nome": nome, "telefone": telefone, "email": email})
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n--- LISTA DE CLIENTES ---")
    for i, c in enumerate(clientes, start=1):
        print(f"{i}. Nome: {c['nome']} | Tel: {c['telefone']} | Email: {c['email']}")

def atualizar_cliente():
    listar_clientes()
    try:
        indice = int(input("Digite o número do cliente a atualizar: ")) - 1
        if 0 <= indice < len(clientes):
            clientes[indice]['nome'] = input("Novo nome: ")
            clientes[indice]['telefone'] = input("Novo telefone: ")
            clientes[indice]['email'] = input("Novo email: ")
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def excluir_cliente():
    listar_clientes()
    try:
        indice = int(input("Digite o número do cliente a excluir: ")) - 1
        if 0 <= indice < len(clientes):
            clientes.pop(indice)
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# CRUD Pedidos
def criar_pedido():
    global proximo_id
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n--- CLIENTES DISPONÍVEIS ---")
    for i, c in enumerate(clientes, start=1):
        print(f"{i}. {c['nome']} | Tel: {c['telefone']} | Email: {c['email']}")
    try:
        indice_cliente = int(input("Escolha o número do cliente: ")) - 1
        if not (0 <= indice_cliente < len(clientes)):
            print("Cliente inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return
    cliente = clientes[indice_cliente]
    itens = []
    while True:
        mostrar_produtos()
        codigo = input("Digite o código do produto (ou ENTER para finalizar): ").strip()
        if not codigo:
            break
        produto = next((p for p in produtos if p[0] == codigo), None)
        if produto:
            try:
                quantidade = int(input("Digite a quantidade: "))
                itens.append({
                    "codigo": produto[0],
                    "nome": produto[1],
                    "quantidade": quantidade,
                    "preco": produto[2]
                })
            except ValueError:
                print("Quantidade inválida.")
        else:
            print("Produto não encontrado.")
    if itens:
        pedidos.append({
            "id": proximo_id,
            "cliente": cliente['nome'],
            "itens": itens
        })
        print("Pedido criado com sucesso!")
        proximo_id += 1
    else:
        print("Nenhum item adicionado ao pedido.")

def listar_pedidos():
    print("\n--- PEDIDOS CRIADOS ---")
    for p in pedidos:
        print(f"\nID: {p['id']} | Cliente: {p['cliente']}")
        total = 0
        for item in p["itens"]:
            subtotal = item["quantidade"] * item["preco"]
            total += subtotal
            print(f"  - {item['quantidade']}x {item['nome']} (Código: {item['codigo']}) - Subtotal: R${subtotal:.2f}")
        print(f"Total do pedido: R${total:.2f}")
    if not pedidos:
        print("Nenhum pedido cadastrado.")

def excluir_pedido():
    try:
        id_pedido = int(input("\nDigite o ID do pedido a excluir: "))
        global pedidos
        pedidos = [p for p in pedidos if p["id"] != id_pedido]
        print("\nPedido excluído com sucesso!")
    except ValueError:
        print("ID inválido.")

# Login
while True:
    limpa_tela()
    logo()
    usuario = input('Login: ')
    senha = input('Senha: ')    
    if (usuario, senha) in logins:
        print("Login bem-sucedido!")
        time.sleep(2)
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        time.sleep(2)

# Menu principal
while True:
    limpa_tela()
    logo()
    menu()    
    try:
        escolha = int(input('Qual a escolha?: '))
    except ValueError:
        print("Entrada inválida.")
        time.sleep(2)
        continue

    if escolha == 1:
        limpa_tela()
        while True:
            print("\n--- MENU PEDIDOS ---\n")
            print("1. Criar pedido")
            print("2. Listar pedidos")
            print("3. Excluir pedido")
            print("4. Voltar")
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                limpa_tela()
                criar_pedido()
            elif opcao == "2":
                limpa_tela()
                listar_pedidos()
            elif opcao == "3":
                limpa_tela()
                listar_pedidos()
                excluir_pedido()
            elif opcao == "4":
                print("\nVoltando", end="")
                for _ in range(5):
                    time.sleep(0.2)
                    print(".", end="", flush=True)  
                break
            else:
                print("Opção inválida.")
            input("\nPressione ENTER para continuar...")

    elif escolha == 2:
        limpa_tela()
        while True:
            print("\n--- MENU CLIENTES ---")
            print("1. Cadastrar cliente")
            print("2. Listar clientes")
            print("3. Atualizar cliente")
            print("4. Excluir cliente")
            print("5. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                cadastrar_cliente()
            elif opcao == '2':
                listar_clientes()
            elif opcao == '3':
                atualizar_cliente()
            elif opcao == '4':
                excluir_cliente()
            elif opcao == '5':
                print("\nVoltando", end="")
                for _ in range(5):
                    time.sleep(0.2)
                    print(".", end="", flush=True)
                break
            else:
                print("Opção inválida.")
            input("\nPressione ENTER para continuar...")

    elif escolha == 3:
        limpa_tela()
        while True:
            print("\n--- PRODUTOS ---")
            print("1. Ver produtos")
            print("2. Adicionar produto")
            print("3. Atualizar produto")
            print("4. Deletar produto")
            print("5. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                mostrar_produtos()
            elif opcao == '2':
                adicionar_produto()
            elif opcao == '3':
                atualizar_produto()
            elif opcao == '4':
                deletar_produto()
            elif opcao == '5':
                print("\nVoltando", end="")
                for _ in range(5):
                    time.sleep(0.2)
                    print(".", end="", flush=True)  
                break
            else:
                print("Opção inválida.")
            input("\nPressione ENTER para continuar...")

    elif escolha == 4:
        sai()
    else:
        print("Opção inválida.")
        time.sleep(2)

