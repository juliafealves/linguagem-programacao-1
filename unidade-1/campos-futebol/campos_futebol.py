# coding: utf-8
# Campos Futebol
# (C) 2017, Júlia Alves / UFCG Programação 1

area_campo = 4000.0

# Entrada dos dados referente as áreas
area1 = float(raw_input())
area2 = float(raw_input())
area3 = float(raw_input())

# Calculando as áreas de futebol.
campo1 = area1 / area_campo
campo2 = area2 / area_campo
campo3 = area3 / area_campo

# Calculando a média.
campo_media = (campo1 + campo2 + campo3) / 3

# Imprimindo os resultados.
print '%.2f' % campo1
print '%.2f' % campo2
print '%.2f' % campo3
print '%.2f' % campo_media
