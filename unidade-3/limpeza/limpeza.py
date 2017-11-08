# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Limpeza - Unidade 3

# Definindo as constantes para as opções.
OPCAO_FOSSA = 1
OPCAO_CAIXA_DAGUA = 2
OPCAO_CAIXA_GORDURA = 3

limpeza_fossa = 80.00
limpeza_caixa = 50.00
limpeza_caixa_gordura = 50.00
valor_brinde = 200.00

# Escolhendo a opção de serviço.
opcao = int(raw_input())
preco = limpeza_caixa_gordura

if opcao == OPCAO_FOSSA or opcao == OPCAO_CAIXA_DAGUA:
    volume = float(raw_input())

    # Calculando o preço do serviço de acordo com a opção.
    if opcao == OPCAO_FOSSA:
        preco = volume * limpeza_fossa
    else:
        preco = volume * limpeza_caixa

print "R$ %.0f,00" % preco

# Verifica se o usuário terá direito ao brinde.
if preco >= valor_brinde:
    print "Brinde!"