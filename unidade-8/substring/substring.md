# Verificando se uma String é Substring de Outra String
Escreva uma função `is_substring(str1, str2)` que verifica se `str2` está em `str1`. Em caso afirmativo, a função deve 
retornar `True`. Caso contrário, deve retornar `False`.

### Atenção

Você pode usar `if`, mas não é permitido utilizar o comando `if` em conjunto com o `in`.

## Exemplos e asserts

```
assert is_substring('boiada','oi')
assert not is_substring('casorio', 'casa')
```