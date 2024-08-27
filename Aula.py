clientes = []
def adicionar_cliente(nome, email, telefone, endereco):
   cliente = [nome, email, telefone, endereco]
   clientes.append(cliente)
   print(f" Cliente {nome} cadastrado!")

def exibir_clientes():
   for cliente in clientes:
       print(f"nome: {cliente[0]}, email: {cliente [1]}, telefone: {cliente [2]}, endereço: {cliente [3]}")

def remover_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            clientes.remove(cliente)
            print(f"Cliente com email: {email}, foi removido")
            return 
    print("Cliente não encontrado")

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"nome: {cliente[0]}, email: {cliente [1]}, telefone: {cliente [2]}, endereço: {cliente [3]}")
            return
        print("Cliente encontrado")

def menu():

    while True:
        print("MENU")
        print("1 - ADD")
        print("2 - exib")
        print("3 - BUSCAR")
        print("4 - REMOVER")
        print("5 - SAIR")
        
        opcao = input("Escolha uma opção")

        if opcao == '1':
            nome = input("Entre com nome:")
            email = input("Entre com email:")
            telefone = input("Entre com telefone:")
            endereco = input("Entre com endereço:")
            adicionar_cliente(nome, email, telefone, endereco)

        elif opcao == '2':
            exibir_clientes()

        elif opcao == '3':
           remover_cliente(email)
           email = input("Digite o email do cliente:")

        elif opcao == '4':
            buscar_cliente(email)
            email = input("Digite o email do cliente que será removido:")

        elif opcao == '5':
            print("Saindo do programa")   
            break
               

        else:
            print("Opção invalida")

menu()            
