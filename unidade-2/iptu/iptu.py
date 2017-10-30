# coding: utf-8
# IPTU
# (C) 2017, Júlia Alves / UFCG Programação 1

taxa_limpeza = 35.0
desconto_cota_unica = 0.75
desconto_parcelado6x = 0.95

# Entrada dos dados
area_casa = float(raw_input("Área construída? "))
aliquota = float(raw_input("Alíquota? "))

# Calculando valor do iptu
iptu = area_casa * aliquota + taxa_limpeza
iptu_avista = iptu * desconto_cota_unica

# Calulando parcelamento
iptu_parcelada6x = iptu * desconto_parcelado6x
parcela_6x = iptu_parcelada6x / 6
parcela_10x = iptu / 10

# Imprimindo o valor das passagens e forma de pagamento
print "IPTU: R$ %.2f\n" % iptu
print "Pagamento:\n1. Quota única. R$ %.2f" % iptu_avista
print "2. Em 6 parcelas. Total: R$ %.2f" % iptu_parcelada6x
print "   6 x R$ %.2f" % parcela_6x
print "3. Em 10 parcelas. Total: R$ %.2f" % iptu
print "   10 x R$ %.2f" % parcela_10x