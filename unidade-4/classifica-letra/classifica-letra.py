# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Classifica Letra - Unidade 4

# Recebe a palavra como entrada.
palavra = raw_input()

for letra in palavra:
    letra_minuscula = letra.lower()

    # Verifica se a letra em minúsculo é vogal.
    if letra_minuscula == 'a' or letra_minuscula == 'e' or letra_minuscula == "i"\
            or letra_minuscula == "o" or letra_minuscula == "u":
        print "<%s> sim" % letra
    else:
        print "<%s> nao" % letra
