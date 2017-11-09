# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Segundo - Unidade 3

# Entrada dos números.
numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
numero4 = int(raw_input())

# Verifica qual é o segundo menor e o segundo maior
if (numero3 <= numero1 <= numero2 <= numero4) or (numero4 <= numero1 <= numero2 <= numero3):
    segundo_menor = numero1
    segundo_maior = numero2
elif (numero2 <= numero1 <= numero3 <= numero4) or (numero4 <= numero1 <= numero3 <= numero2):
    segundo_menor = numero1
    segundo_maior = numero3
elif (numero2 <= numero1 <= numero4 <= numero3) or (numero2 <= numero1 <= numero4 <= numero3):
    segundo_menor = numero1
    segundo_maior = numero4
elif (numero3 <= numero2 <= numero1 <= numero4) or (numero4 <= numero2 <= numero1 <= numero3):
    segundo_menor = numero2
    segundo_maior = numero1
elif (numero1 <= numero2 <= numero3 <= numero4) or (numero4 <= numero2 <= numero3 <= numero1):
    segundo_menor = numero2
    segundo_maior = numero3
elif (numero1 <= numero2 <= numero4 <= numero3) or (numero3 <= numero2 <= numero4 <= numero1):
    segundo_menor = numero2
    segundo_maior = numero4
elif (numero2 <= numero3 <= numero1 <= numero4) or (numero4 <= numero3 <= numero1 <= numero2):
    segundo_menor = numero3
    segundo_maior = numero1
elif (numero1 <= numero3 <= numero2 <= numero4) or (numero4 <= numero3 <= numero2 <= numero1):
    segundo_menor = numero3
    segundo_maior = numero2
elif (numero1 <= numero3 <= numero4 <= numero2) or (numero2 <= numero3 <= numero4 <= numero1):
    segundo_menor = numero3
    segundo_maior = numero4
elif (numero2 <= numero4 <= numero1 <= numero3) or (numero3 <= numero4 <= numero1 <= numero2):
    segundo_menor = numero4
    segundo_maior = numero1
elif (numero3 <= numero4 <= numero2 <= numero1) or (numero1 <= numero4 <= numero2 <= numero3):
    segundo_menor = numero4
    segundo_maior = numero2
elif (numero1 <= numero4 <= numero3 <= numero2) or (numero2 <= numero4 <= numero3 <= numero1):
    segundo_menor = numero4
    segundo_maior = numero3

# Imprime a informação sobre o segundo menor e segundo maior.
print "Considerando os números %i, %i, %i e %i" % (numero1, numero2, numero3, numero4)
print "O segundo menor número é %i" % segundo_menor
print "O segundo maior número é %i" % segundo_maior