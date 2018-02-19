# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Grep - Unidade 4

palavra_chave = raw_input()
tamanho_palavra = len(palavra_chave)

quantidade_frases = int(raw_input())
achou_palavra = False

for entrada in range(quantidade_frases):
    frase = raw_input()
    tamanho_frase = len(frase)

    if tamanho_frase <= tamanho_palavra:
        if frase == palavra_chave:
            print frase
    else:
        for i in range(tamanho_frase - 2):
            palavra = ""

            for j in range(i, i + tamanho_palavra):
                palavra += frase[j]
                if palavra == palavra_chave and not achou_palavra:
                    achou_palavra = True
                    print frase
