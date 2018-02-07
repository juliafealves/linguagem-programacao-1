# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Cria Senha - Unidade 7


# Retorna um senha mais forte do que a informada, substituindo algumas letras por números.
def gerar_senha_forte(senha):
    nova_senha = ""

    for letra in senha:
        letra_minuscula = letra.lower()

        if letra_minuscula == "o":
            nova_senha += "0"
        elif letra_minuscula == "i" or letra_minuscula == "l":
            nova_senha += "1"
        elif letra_minuscula == "e":
            nova_senha += "3"
        elif letra_minuscula == "a":
            nova_senha += "4"
        elif letra_minuscula == "b":
            nova_senha += "6"
        elif letra_minuscula == "t":
            nova_senha += "7"
        else:
            nova_senha += letra

    return nova_senha


# Delimita um string com prefixo e sufixo informado.
def delimitar_string(string, prefixo="((", sufixo="))"):
    return prefixo + string + sufixo


# O tipo "fraco" corresponde a senha "Fácil ou Fraca" e o tipo "forte" corresponde a senha "Difícil ou Forte".
def gerar_senha(senha, tipo):
    if tipo == "fraco":
        return delimitar_string(senha)
    elif tipo == "forte":
        senha_forte = gerar_senha_forte(senha)

        return delimitar_string(senha_forte)


# Main do Programa.
entrada = raw_input()

while entrada != "***":
    entradas = entrada.split()
    print gerar_senha(entradas[0], entradas[1])
    entrada = raw_input()