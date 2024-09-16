# -*- coding: utf-8 -*-
import random
import string


def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits  # Letras e dígitos
    return ''.join(random.choice(caracteres) for _ in range(tamanho))


def cifra_cesar_recursiva(senha, pos=0):
    if pos == len(senha):
        return ""
    else:
        char_atual = senha[pos]


        if char_atual.isalpha():
            if char_atual.islower():
                novo_char = chr((ord(char_atual) - ord('a') + 3) % 26 + ord('a'))
            else:
                novo_char = chr((ord(char_atual) - ord('A') + 3) % 26 + ord('A'))

        elif char_atual.isdigit():
            novo_char = chr((ord(char_atual) - ord('0') + 3) % 10 + ord('0'))
        else:
            novo_char = char_atual


        return novo_char + cifra_cesar_recursiva(senha, pos + 1)


tamanho_senha = 8
senha_original = gerar_senha(tamanho_senha)
senha_criptografada = cifra_cesar_recursiva(senha_original)


print(f"Senha original: {senha_original}")
print(f"Senha criptografada: {senha_criptografada}")
