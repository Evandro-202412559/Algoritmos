#1. Tratamento de exceções básicas: Escreva um programa que peça ao usuário
# dois números e faça a divisão do primeiro pelo segundo. Se o usuário inserir
# um valor inválido ou tentar dividir por zero, o programa deve exibir uma
# mensagem de erro apropriada.

def div (num1, num2):
     divisao=num1 / num2
     return (divisao)

try:
     num1 = int(input("DIGITE O PRIMEIRO NUMERO:"))
     num2 = int(input("DIGITE O SEGUNDO NUMERO:"))
     resultado = div(num1, num2)
     print(resultado)
    

except ZeroDivisionError:
     print("NÃO É POSSIVEL DIVIDIR POR ZERO!")


except ValueError:
     print("DIGITE UM VALOR VALIDO.")   






#2. Capturando exceções múltiplas: Crie um programa que peça ao usuário o
# nome de uma cor e mostre seu valor em RGB de acordo com um dicionário
# pré-definido. O programa deve tratar exceções caso o nome da cor não exista
# no dicionário.
# cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul':
# (0, 0, 255)}


cores = {
     'vermelho': (255, 0, 0),
     'verde': (0, 255, 0),
     'azul': (0, 0, 255)
 }

def buscar_cor():
     try:
        
        nome_cor = input("Digite o nome de uma cor (vermelho, verde, azul): ").lower()
        
        
        rgb = cores[nome_cor]
        
        
        print(f"O valor RGB de {nome_cor} é {rgb}.")
        
     except KeyError:
        
         print(f"Erro: A cor {nome_cor} não foi encontrada no dicionário.")
   


buscar_cor()


#3. Bloco else e finally: Escreva um programa que solicite um número ao
# usuário. Se o número for maior que 10, exiba uma mensagem dizendo que o
# número é válido. Utilize o bloco else para imprimir que o programa foi
# executado com sucesso, e o bloco finally para imprimir "Programa
# encerrado".

def numero(num):
     if num >= 10:
         print("NUMERO VALIDO.")

     else:
        print("PROGRAMA EXECUTADO COM SUCESSO!")    

        return num
    
try:

    num = int(input("DIGITE UM NUMERO:"))
     
    resultado = numero(num)
    print(resultado)

finally:
    print("PROGRAMA ENCERRADO.")



#4. Exceções personalizadas: Escreva uma função que verifica se uma senha
# possui no mínimo 8 caracteres e pelo menos um número. Se a senha não
# atender aos requisitos, levante uma exceção com uma mensagem
# personalizada. Trate a exceção e mostre a mensagem ao usuário.

class SenhaInvalidaError(Exception):
     def init (self, mensagem):
         self.mensagem = mensagem
         super().init(self.mensagem)
        
def verificar_senha(senha):
     if len(senha) < 8:
        
         raise SenhaInvalidaError("Erro: A senha deve ter no mínimo 8 caracteres.")
    
     if not any(char.isdigit() for char in senha):
        
        raise SenhaInvalidaError("Erro: A senha deve conter pelo menos um número.")
    
    
     print("Senha válida!")


def main():
    try:
         senha = input("Digite a sua senha: ")
         verificar_senha(senha)  
    except SenhaInvalidaError as e:
        
         print(e)


main()
    
    

#5. Simulação de transações: Crie um programa que simule uma transferência
# bancária. Peça ao usuário o saldo da conta e o valor da transferência. Caso o
# saldo seja insuficiente, levante uma exceção do tipo ValueError com a
# mensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o
# usuário.


def transferencia_bancaria(saldo, valor_transferencia):
    if valor_transferencia > saldo:
        
        raise ValueError("Saldo insuficiente")
    
    
    saldo -= valor_transferencia
    print(f"Transferência realizada com sucesso! Saldo atual: R${saldo:.2f}")


def main():
    try:
        
        saldo = float(input("Informe o saldo da conta: R$"))
        valor_transferencia = float(input("Informe o valor da transferência: R$"))
        
        
        transferencia_bancaria(saldo, valor_transferencia)
    
    except ValueError as e:
        
        print(e)


main()
