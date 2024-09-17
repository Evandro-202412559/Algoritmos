

def potencia(base, expoente):

    if expoente == 0:
        return 1
    elif expoente == 1:
        return base
    else:
        return base * potencia(base, expoente - 1)

#Teste
print(potencia(2, 3))

def fibonacci(n):

   if n < = 1:
       return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Teste
print(fibonacci(5))

def contar_digitos(numero):

    if abs(numero) < 10:
        return 1

    else:
        return 1 + contar_digitos(numero // 10)

#Teste
print(contar_digitos(12345))

def eh_palindromo(string):

        return True

        if len(string) <= 1:

         return True

        elif string[0] != string[-1]:
         return False

        else:
         return eh_palindromo(string[1:-1])

#Teste
print(eh_palindromo("radar"))  # Saída: True
print(eh_palindromo("python"))  # Saída: False
