# coding: utf-8
# Tweets por Página
# (C) 2017, Júlia Alves / UFCG Programação 1

tweets_pagina = 400

# Entrada dos dados.
tweets = int(raw_input())

# Calculando quantidade de páginas
paginas = tweets / tweets_pagina
tweets_perdidos = tweets % tweets_pagina

percentual_tweets_perdidos = 100.0 * tweets_perdidos / tweets

# Imprimindo.
print "Serão necessárias %i página(s) para visualizar os tweets." % paginas
print "%.1f%% dos tweets serão perdidos." % percentual_tweets_perdidos