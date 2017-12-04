# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Semi César - Unidade 6

# Criptografa a mensagem deslocando n para direita em relação ao alfabeto.
def cesar(mensagem, deslocamento):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    tamanho_alfabeto = len(alfabeto)
    criptografia = ""

    for caracter in mensagem:
        caracter_encontrado = False

        for indice in range(tamanho_alfabeto):
            if caracter == alfabeto[indice]:
                valor_deslocar = deslocamento + indice

                # Condicional para deslocamento ciclico.
                if  valor_deslocar > (tamanho_alfabeto - 1):
                    valor_deslocar = valor_deslocar - tamanho_alfabeto

                criptografia += alfabeto[valor_deslocar]
                caracter_encontrado = True
        
        # Caso não seja um caracter válido.
        if not(caracter_encontrado):
            criptografia += caracter
    
    return criptografia
