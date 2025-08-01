import time
import os

logins = [('admin', '1234'), ('Samuel', '1234')]
produtos = [['1', 'café preto', 3],['2', 'café exprsso', 5]]
pedidos =[]
proximo_id = 1

def logo():
    print('-'*33)
    print('='*5, 'COFFEE SHOPS TIA ROSA', '='*5)
    print('-'*33)

def menu():
    print("-" * 30)
    print('1 - Pedido\n'
    '2 - Cadastro Cliente\n' 
    '4 - Produtos\n'
    '5 - Sair') 

def sai(): 
    print("\nEncerrando", end="")
    for _ in range(5):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print('\n')
    print('-'*33)
    print('='*5, 'COFFEE SHOPS TIA ROSA', '='*5)
    print('-'*33)
    quit()

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# CRUD Produtos

def mostrar_produtos():
    
    print("\nCódigo".ljust(10) + "Produto".ljust(20) + "Preço (R$)")
    print("-" * 40)

    for codigo, nome, preco in produtos:
        print(codigo.ljust(10) + nome.ljust(20) + f"R$ {preco:.2f}")

def adicionar_produto():
    codigo = input("Código: ")
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

# CRUD PEDIDOS

def criar_pedido():
    global proximo_id
    mostrar_produtos()
    codigo = input("Digite o código do produto: ").strip()
    produto = next((p for p in produtos if p[0] == codigo), None)
    if produto:
        try:
            quantidade = int(input("Digite a quantidade: "))
            pedidos.append({
                "id": proximo_id,
                "codigo": produto[0],
                "nome": produto[1],
                "quantidade": quantidade,
                "preco": produto[2]
            })
            print("Pedido criado com sucesso!")
            proximo_id += 1
        except ValueError:
            print("Quantidade inválida.")
    else:
        print("Produto não encontrado.")

def listar_pedidos():
    if not pedidos:
        print("Nenhum pedido cadastrado.")
        return
    print("\nPedidos:")
    for p in pedidos:
        total = p["quantidade"] * p["preco"]
        print(f"ID: {p['id']} | {p['quantidade']}x {p['nome']} (Código: {p['codigo']}) - Total: R${total}")

def excluir_pedido():
    try:
        id_pedido = int(input("Digite o ID do pedido a excluir: "))
        global pedidos
        pedidos = [p for p in pedidos if p["id"] != id_pedido]
        print("Pedido excluído com sucesso!")
    except ValueError:
        print("ID inválido.")

while True:
    limpa_tela()

    logo()
    
    usuario = input('Login:')
    senha = input('Senha:')    
    if (usuario, senha) in logins:
        print("Login bem-sucedido!")
        time.sleep(3)
        break
    else:
        print("Usuário ou senha incorretos.Tente novamente")
        time.sleep(2)

while True:
    limpa_tela()

    logo()

    menu()    
    
    escolha = int(input('Qual a escolha?: '))
    
    if escolha == 1:
        while True:
            print("\n--- PEDIDOS ---")
            print("1. Criar pedido")
            print("2. Listar pedidos")
            print("3. Excluir pedido")
            print("4. Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                criar_pedido()
            elif opcao == "2":
                listar_pedidos()
            elif opcao == "3":
                excluir_pedido()
            elif opcao == "4":
                print("\nVoltando", end="")
                for _ in range(5):
                    time.sleep(0.2)
                    print(".", end="", flush=True)  
                break
            else:
                print("Opção inválida.")

    elif escolha == 4:
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
    elif escolha == 5:
        sai()