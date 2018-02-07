# Único

Escreva a função unico(string) que recebe uma string e retorna uma string formada a partir da string original pela substituição da sucessão de ocorrências (consecutivas) de um mesmo caractere por esse caractere. Não utilizar nenhuma lista auxiliar. Por simplificação, assuma que a string não possui nem caracteres acentuados nem letras maiúsculas.

## Exemplos de asserts

assert unico("aa***xxxzzb+++") == "a*xzb+"
assert unico("") == ""
