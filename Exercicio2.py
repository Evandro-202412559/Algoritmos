clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "endereco": endereco
    }
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado!")

def exibir_clientes():
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}, Endereço: {cliente['endereco']}")

def remover_cliente(email):
    for cliente in clientes:
        if cliente["email"] == email:
            clientes.remove(cliente)
            print(f"Cliente com email: {email} foi removido")
            return
    print("Cliente não encontrado")

def buscar_cliente(email):
    for cliente in clientes:
        if cliente["email"] == email:
            print(f"Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}, Endereço: {cliente['endereco']}")
            return
    print("Cliente não encontrado")

def menu():
    while True:
        print("MENU")
        print("1 - Adicionar Cliente")
        print("2 - Exibir Clientes")
        print("3 - Buscar Cliente")
        print("4 - Remover Cliente")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Entre com nome: ")
            email = input("Entre com email: ")
            telefone = input("Entre com telefone: ")
            endereco = input("Entre com endereço: ")
            adicionar_cliente(nome, email, telefone, endereco)

        elif opcao == '2':
            exibir_clientes()

        elif opcao == '3':
            email = input("Digite o email do cliente: ")
            buscar_cliente(email)

        elif opcao == '4':
            email = input("Digite o email do cliente que será removido: ")
            remover_cliente(email)

        elif opcao == '5':
            print("Saindo do programa")
            break

        else:
            print("Opção inválida")

menu()
