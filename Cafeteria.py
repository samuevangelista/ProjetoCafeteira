import time
import os

logins = [('admin', '1234'), ('Samuel', '1234')]
produtos = [['1', 'café preto', 3], ['2', 'café expresso', 5]]
pedidos = []
clientes = []
proximo_id = 1

def logo(): # Função para mostrar logo
    print('-'*33)
    print('='*5, 'COFFEE SHOPS TIA ROSA', '='*5)
    print('-'*33)

def menu(): # Função para mostrar menu
    print("-" * 30)
    print('1 - Pedido\n'
          '2 - Cadastro Cliente\n'
          '3 - Produtos\n'
          '4 - Sair')

def sai(): # Função para sair do sistema
    print("\nEncerrando", end="")
    for _ in range(5):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print('\n')
    print('-'*33)
    print('='*5, 'COFFEE SHOPS TIA ROSA', '='*5)
    print('-'*33)
    quit()

def limpa_tela(): # Função para limpar tela (Apenas para deixar menos poluído)
    os.system('cls' if os.name == 'nt' else 'clear')

# CRUD Produtos
def mostrar_produtos(): #Função para mostar os produtos
    print("\nCódigo".ljust(10) + "Produto".ljust(20) + "Preço (R$)")
    print("-" * 40)
    for codigo, nome, preco in produtos:
        print(codigo.ljust(10) + nome.ljust(20) + f"R$ {preco:.2f}")
    print("-" * 40)

def adicionar_produto(): # função para adicionar produtos
    codigo = input("Código: ")
    if any(p[0] == codigo for p in produtos):
        print("Código já existente. Tente outro.")
        return
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    produtos.append([codigo, nome, preco])
    print("Produto adicionado com sucesso!")

def atualizar_produto(): # função para atualizar produtos
    codigo = input("Digite o código do produto a atualizar: ")
    for produto in produtos:
        if produto[0] == codigo:
            produto[1] = input("Novo nome: ")
            produto[2] = float(input("Novo preço: "))
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def deletar_produto(): # função para excluir produto
    codigo = input("Digite o código do produto a deletar: ")
    for produto in produtos:
        if produto[0] == codigo:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")


# CRUD Pedidos
def criar_pedido(): # Função para criar novo pedido, adicionando cliente ao pedido
    global proximo_id

    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente antes de fazer pedidos.")
        return

    print("\n--- CLIENTES DISPONÍVEIS ---")
    for i, c in enumerate(clientes, start=1):
        print(f"{i}. {c['nome']} | Tel: {c['telefone']} | Email: {c['email']}")

    try:
        indice_cliente = int(input("\nEscolha o número do cliente: ")) - 1
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
            print('Código não encontrado')
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


def listar_pedidos(): # função para listar os pedidos
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

def excluir_pedido(): # funcão para excluir pedido 
    try:
        id_pedido = int(input("\nDigite o ID do pedido a excluir: "))
        global pedidos
        pedidos = [p for p in pedidos if p["id"] != id_pedido]
        print("\nPedido excluído com sucesso!")
    except ValueError:
        print("ID inválido.")


# CRUD Clientes
def cadastrar_cliente(): # função para criar cliente
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    clientes.append({
        "nome": nome,
        "telefone": telefone,
        "email": email
    })
    print("Cliente cadastrado com sucesso!")

def listar_clientes(): # função para listar cliente
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n--- LISTA DE CLIENTES ---")
    for i, c in enumerate(clientes, start=1):
        print(f"{i}. Nome: {c['nome']} | Telefone: {c['telefone']} | Email: {c['email']}")

def atualizar_cliente(): # função para atualizar cliente
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

def excluir_cliente(): # função para excluir cliente
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

# Login
while True: # Faz um login simples no sistema
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

# Menu Principal
while True: # Loop do programa
    limpa_tela()
    logo()
    menu()
    try:
        escolha = int(input('Qual a escolha?: '))
    except ValueError:
        print("Por favor, digite um número válido.")
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
                print("Opção inválida. Tente novamente.")

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
                print("Opção inválida. Tente novamente.")

    elif escolha == 4:
        sai()
        
    else:
        print("Opção inválida.")
        time.sleep(2)