produtos = [
    ("001", "joao", 25),
    ("002", "maria", 30),
    ("003", "pedro", 22)
]

pedidos = []
proximo_id = 1

def listar_produtos():
    print("\nProdutos disponíveis:")
    for codigo, nome, preco in produtos:
        print(f"Código: {codigo} | Nome: {nome} | Preço: R${preco}")

def criar_pedido():
    global proximo_id
    listar_produtos()
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

def atualizar_pedido():
    try:
        id_pedido = int(input("Digite o ID do pedido a atualizar: "))
        pedido = next((p for p in pedidos if p["id"] == id_pedido), None)
        if pedido:
            nova_qtd = int(input("Digite a nova quantidade: "))
            pedido["quantidade"] = nova_qtd
            print("Pedido atualizado com sucesso!")
        else:
            print("Pedido não encontrado.")
    except ValueError:
        print("ID inválido.")

def excluir_pedido():
    try:
        id_pedido = int(input("Digite o ID do pedido a excluir: "))
        global pedidos
        pedidos = [p for p in pedidos if p["id"] != id_pedido]
        print("Pedido excluído com sucesso!")
    except ValueError:
        print("ID inválido.")

# Menu principal
while True:
    print("\n--- MENU ---")
    print("1. Criar pedido")
    print("2. Listar pedidos")
    print("3. Atualizar pedido")
    print("4. Excluir pedido")
    print("5. Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        criar_pedido()
    elif opcao == "2":
        listar_pedidos()
    elif opcao == "3":
        atualizar_pedido()
    elif opcao == "4":
        excluir_pedido()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
