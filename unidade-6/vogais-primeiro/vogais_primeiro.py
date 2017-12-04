# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Vogais Primeiro - Unidade 6

# Recebe uma frase e coloca as vogais antes 
# que as consoantes na ordem que aparecem
def vogais_primeiro(frase):
    vogais = ""
    consoantes = ""

    for letra in frase:
        if letra in "aeiou":
            vogais += letra
        else:
            consoantes += letra
    
    return vogais + consoantes
