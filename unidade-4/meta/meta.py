# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Meta - Unidade 4

# Guarda as vendas dos funcionários.
vendas_funcionarios = [0, 0, 0, 0, 0, 0]

# Recebe a meta de venda da loja.
meta_venda = float(raw_input())

# Calcula a meta individual dos funcionários.
meta_individual = meta_venda / 6

total_venda = 0
meta_atingida = True

# Recebe as vendas dos 6 funcionários e verifica se atingiu a meta de venda.
for n in range(6):
    vendas_funcionarios[n] = float(raw_input())
    total_venda += vendas_funcionarios[n]

    if meta_atingida and meta_individual > vendas_funcionarios[n]:
        meta_atingida = False

# Imprime o resultado de acordo com a meta atiginda.
if meta_atingida:
    print "Total de vendas: R$ %.2f (meta atingida)" % total_venda
    print "----\nBonificação:"

    i = 1
    for venda_funcionario in vendas_funcionarios:
        bonificacao = venda_funcionario * 0.01
        print "Funcionário %i: R$ %.2f" % (i, bonificacao)
        i += 1
else:
    print "Total de vendas: R$ %.2f (meta não foi atingida)" % total_venda
    print "----"
