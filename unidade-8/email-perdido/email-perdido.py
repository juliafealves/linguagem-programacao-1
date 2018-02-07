# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Email Perdido - Unidade 8


# Verifica se existe um e-mail em uma lista de e-mails.
def existe_email(email, emails):
    for mail in emails:
        if email == mail:
            return True

    return False


# Retorna o e-mail que foi enviado e não foi recebido.
def encontra_email_perdido(emails_enviados, emails_recebidos):
    for i in range(len(emails_enviados) - 1, -1, -1):
        existe = existe_email(emails_enviados[i], emails_recebidos)

        if existe:
            emails_enviados.pop(i)

    return emails_enviados[0]