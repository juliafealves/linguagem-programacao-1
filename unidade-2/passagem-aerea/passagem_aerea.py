# coding: utf-8
# Passagem Aérea
# (C) 2017, Júlia Alves / UFCG Programação 1

taxa_aeroporto = 51.0
desconto_avista = 0.75
desconto_parcelado6x = 0.95

# Entrada dos dados
milhas = float(raw_input())
aliquota = float(raw_input())

# Calculando valor da passagem
passagem = milhas * aliquota + taxa_aeroporto
passagem_avista = passagem * desconto_avista

# Calulando parcelamento
passagem_parcelada6x = passagem * desconto_parcelado6x
parcela_6x = passagem_parcelada6x / 6
parcela_10x = passagem / 10

# Imprimindo o valor das passagens e forma de pagamento
print "Valor da passagem: R$ %.2f\n" % passagem
print "Pagamento:\n1. À vista. R$ %.2f" % passagem_avista
print "2. Em 6 parcelas. Total: R$ %.2f" % passagem_parcelada6x
print "   6 x R$ %.2f" % parcela_6x
print "3. Em 10 parcelas. Total: R$ %.2f" % passagem
print "   10 x R$ %.2f" % parcela_10x
