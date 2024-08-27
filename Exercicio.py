

clientes = []


def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)
    print(f"Cliente {nome} adicionado com sucesso!\n")


def exibir_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.\n")
    else:
        print("Lista de Clientes:")
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. Nome: {cliente[0]}, Email: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")
        print()  

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Cliente encontrado: Nome: {cliente[0]}, Email: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}\n")
            return cliente
    print(f"Cliente com o email {email} não encontrado.\n")
    return None


def remover_cliente(email):
    cliente = buscar_cliente(email)
    if cliente:
        clientes.remove(cliente)
        print(f"Cliente com o email {email} removido com sucesso!\n")


def main():
    while True:
        print("Menu de Opções:")
        print("1. Adicionar Cliente")
        print("2. Exibir Clientes")
        print("3. Buscar Cliente por E-mail")
        print("4. Remover Cliente")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o e-mail do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            adicionar_cliente(nome, email, telefone, endereco)
        
        elif opcao == '2':
            exibir_clientes()
        
        elif opcao == '3':
            email = input("Digite o e-mail do cliente a ser buscado: ")
            buscar_cliente(email)
        
        elif opcao == '4':
            email = input("Digite o e-mail do cliente a ser removido: ")
            remover_cliente(email)
        
        elif opcao == '5':
            print("Encerrando o sistema...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

if __name__ == "__main__":
    main()
