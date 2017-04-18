# testando as funcoes criadas do arquivo funcs

# o comando abaixo importa todas as funcoes do modulo funcs, o asteriscos pede todas as funcoes
# se usar 'from funcs import soma' importa so a funcao soma do modulo funcs

from funcs import *

a = 2
b = 3

print soma(a, b)


# caso precise importar um modulo dentro de um outro diretorio, precisa criar um arquivo chamado __init__.py
# dentro desse diretorio

# no exemplo abaixo tem a pasta Modulo_criado, dentro tem a pasta App, e funcs esta dentro da mesma
# para ele entrar nas pastas, coloquei um arquivo __init__.py nas duas pastas

from Modulo_criado.App.funcs import *