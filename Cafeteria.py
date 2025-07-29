import time
import os

logins = [('admin', '1234'), ('Samuel', '1234')]
produtos = [['café preto', 3]]
pedidos =[]

def mostra_menu():
    print("-" * 30)
    print('1 - Pedido\n'
    '2 - Cadastro Cliente\n' 
    '3 - Cadastro Produto\n'
    '4 - Produtos\n'
    '5 - Sair') 

def sai(): 
    print("\nEncerrando", end="")
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print('\n')
    print('-'*33)
    print('='*5, 'COFFEE SHOPS TIA ROSA', '='*5)
    print('-'*33)
    quit()

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostra_produtos():
    print("Produto".ljust(20) + "Preço (R$)")
    print("-" * 30)
    for nome, preco in produtos:
        print(nome.ljust(20) + f"R$ {preco:.2f}")



while True:
    limpa_tela()

    print('-'*33)
    print('='*5, 'COFFEE SHOPS TIA ROSA', '='*5)
    print('-'*33)
    
    usuario = input('Login:')
    senha = input('Senha:')    
    if (usuario, senha) in logins:
        print("Login bem-sucedido!")
        time.sleep(3)
        break
    else:
        print("Usuário ou senha incorretos.Tente novamente")
        time.sleep(3)

while True:
    limpa_tela()
    print('-'*33)
    print('='*5, 'COFFEE SHOPS TIA ROSA', '='*5)
    print('-'*33)

    mostra_menu()    
    
    escolha = int(input('Qual a escolha?: '))
    
    if escolha == 4:
        mostra_produtos()
        mostra_menu()
    elif escolha == 5:
        sai()