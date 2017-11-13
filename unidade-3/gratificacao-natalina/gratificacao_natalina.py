# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Gratificação Natalina - Unidade 3

# Códigos dos possíveis cargos.
CARGO_PRESIDENTE = '1'
CARGO_DIRETOR = '2'
CARGO_GERENTE = '3'
CARGO_ENGENHEIRO_SENIOR = '4'

codigo_cargo = raw_input()

# Verifca qual o cargo a ser calculada a gratificação natalina.
if codigo_cargo == CARGO_PRESIDENTE or codigo_cargo == CARGO_DIRETOR:
    salario = 15000.00
    if(codigo_cargo == CARGO_PRESIDENTE):
        salario = 25000.00
else:
    # Caso o cargo seja Gerente, Engenheiro Sênior e Júnior solicita a quantidade de faltas para calcular a gratificação natalina.
    faltas = int(raw_input())

    if codigo_cargo == CARGO_GERENTE:
        salario = 8000.00
        gratificacao_dia = 2.00
        gratificacao_natalina = 500.00
    elif codigo_cargo == CARGO_ENGENHEIRO_SENIOR:
        salario = 5000.00 
        gratificacao_dia = 1.00
        gratificacao_natalina = 300.00
    else:
        salario = 2800.00
        gratificacao_dia = 0.70
        gratificacao_natalina = 200.00
    
    # Calcula a gratificação natalina proporcional caso o funcionário tenha faltado.
    if faltas != 0:
        gratificacao_natalina = (235 - faltas) * gratificacao_dia
    
    salario += gratificacao_natalina
    
    # Imprime o valor da graficação nas condições dos cargos Gerente, Engenheiro Sênior e Júnior.
    print "Valor da gratificação R$ %.2f." % gratificacao_natalina

# Imprime o valor do salário.
print "Deverá receber em dezembro R$ %.2f." % salario