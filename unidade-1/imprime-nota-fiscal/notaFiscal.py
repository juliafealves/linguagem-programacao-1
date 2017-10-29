# coding: utf-8
# Imprime Nota Fiscal
# (C) 2017 Júlia Alves / UFCG Programação 1

# Entrada de dados da nota fiscal.
valorTotal = float(raw_input())
data = raw_input()
quantidadeProdutos = int(raw_input())

# Calculando a média de preço dos produtos.
media = valorTotal / quantidadeProdutos

print "Data: %s" % data
print "O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de %.1f." % (valorTotal, media)