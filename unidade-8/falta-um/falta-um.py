# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Falta Um - Unidade 8


# Verifica se um elemento existe em uma lista.
def existe_elemento(elemento, lista):
    for item in lista:
        if elemento == item:
            return True

    return False


# Encontra o rótulo perdido durante o envio.
def encontra_rotulo_perdido(rotulos_enviados, rotulos_recebidos):
    for rotulo in rotulos_enviados:
        if not existe_elemento(rotulo, rotulos_recebidos):
            return rotulo
