# Email Perdido
Nos últimos dias, duas negociantes (Raquel e Carla) trocaram vários emails a respeito de uma transação entre as duas.

Contudo, Carla jura que não recebeu um email que Raquel jura que enviou. E as duas tem razão. Acontece que o servidor de emails perdeu um email enviado por Raquel antes dele chegar na caixa de entrada de Carla. Isso pode ser confirmado porque na lista de emails enviados por Raquel, tem um email que não aparece na lista dos emails recebidos por Carla.

Escreva a função encontra_email_perdido(emails_enviados, emails_recebidos) que retorna o email da lista de enviados que não aparece na lista de emails recebidos.

Você pode assumir que sempre haverá um email que foi enviado por Raquel, mas não foi recebido por Carla.

## Exemplos de asserts
```
l1 = ['oi', 'ola', 'paguei']
l2 = ['ola', 'paguei']
assert encontra_email_perdido(l1,l2) == 'oi'
```