# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Números Oscilantes - Unidade 7


# Caso o valor seja par retorna 0, caso contrário 1.
def is_par_impar(numero):
    if numero % 2 == 0:
        return 0

    return 1


codigo = raw_input()
tamanho_codigo = len(codigo)
mensagem = "verdadeiro"

atual = is_par_impar(int(codigo[0]))

for indice in range(1, tamanho_codigo):
    proximo = is_par_impar(int(codigo[indice]))

    if atual == proximo:
        mensagem = "falso"
        break
    else:
        atual = proximo

print "%s: %i algarismos." % (mensagem, tamanho_codigo)
