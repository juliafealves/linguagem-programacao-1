# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Limpeza - Unidade 3

OPCAO_FOSSA = "1"
OPCAO_CAIXA_DAGUA = "2"
OPCAO_CAIXA_GORDURA = "3"

limpeza_fossa = 80
limpeza_caixa = 50
limpeza_caixa_gordura = 50
valor_brinde = 200
preco = 0

# Escolhendo a opção de serviço.
opcao = raw_input()

if (opcao == OPCAO_FOSSA or opcao == OPCAO_CAIXA_DAGUA):
	volume = int(raw_input())
	
	# Calculando o preço do serviço de acordo com a opção.
	if (opcao == OPCAO_FOSSA):
		preco = volume * limpeza_fossa
	else:
		preco = volume * limpeza_caixa		
else:
	preco = limpeza_caixa_gordura
	
print "R$ %i,00" % int(preco)

if (preco > valor_brinde):
	print "Brinde!"
