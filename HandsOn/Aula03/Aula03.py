# FUNCAO -------

animais = ['tigre', 'boi', 'galinha']

b = 'b'


#for a in animais:
#	print a


# se precisar funcao para exibir varias listas, varias vezes, pode-se usar uma funcao
'''
Para usar uma variavel que esteja no escopo global, preciso usar global para importar para o escopo da funcao
No exemplo abaixo, ele vai printar a lista animais e vai importar a variavel b
Se criar uma variavel dentro da funcao, a variavel nao vai exister no escopo global
'''

def exibir_lista(animais):
	global b
	for a in animais:
		print a


exibir_lista(animais)


# Funcao com parametros obrigatorios
def somar(a, b):
	return a+b

resultado = somar(2, 2) # quando se usa o return na funcao, pode-se armazenar o resultado em uma variavel
print resultado


# Funcao com um parametro opcional b
def somar(a, b=2):
	return a+b

resultado = somar(5) # quando se usa o return na funcao, pode-se armazenar o resultado em uma variavel
print resultado


#
a = int(raw_input('Valor a: '))
b = int(raw_input('Valor b: '))
resultado = somar(a, b)
print resultado
#


# Quando nao se sabe o numero exato de argumentos, usar args (usa lista de argumentos)
def subtrair(*args):
	saida = ''
	for a in args:
		saida = saida + str(a)
	print saida

subtrair(2, 3, 10, 50)


# Quando nao se sabe o numero exato de argumentos, usar kwargs (usa dicionario de argumentos)
# se nao souber se e lista ou dicionario, pode-se usar como abaixo, tanto o args como kwargs
def multiplicar(**kwargs):
	print kwargs

multiplicar(a=2,b=1,c=4,d=6)



# se nao souber se e lista ou dicionario, pode-se usar como abaixo, tanto o args como kwargs
# pode usar o help para ajudar sobre o que se pode colocar neste elemento
# se voce colocar
def multiplicar(*args, **kwargs):
	#print help(kwargs)
	print args

multiplicar(8, 3, 5, a=2,b=1,c=4,d=6) # os valores que nao tem chave (8,3,5) entram so no args e os que tem no kwargs


# FUNCAO LAMBDA -----------------------------------------------------------------------------------------------------
f= lambda x, y, z: x + y + z

print f(1,2,3)

# mesma coisa que fazer com a funcao abaixo:

def somarvarios(x, y, z):
	return x + y + z

print somarvarios(1, 2, 3)



# FUNCAO PARA CONTAR A QUANTIDADE DE CARACTERES EM CADA PALAVRA ---------------------------
words = ['pera', 'uva', 'mamao']

def size(words):
	lista = []
	for e in words:
		lista.append(len(e))
	return lista

print size(words)


# USANDO O LAMBDA PARA A MESMA FUNCAO ACIMA

frutas = lambda words: [len(w) for w in words]
print frutas(words)


# Tratamento de excecoes -------------------------------------------------------------------
# O try abaixo vai dar errado porque a funcao func() nao esta definida em lugar algum
# O try pode ser usado dentro de for, para que nao seja encerrado o script do nada, ele vai dar erro e voltar 
# para o proximo loop do for
# Ele vai executar as funcoes dentro de try, quando achar algum erro ele para a execucao de try
# e vai para a excecao

try:
	print 'Primeira linha'
	func()
	print 3 + 3
except Exception as e:
	print 'Algo de errado aconteceu'




# a funcao pass abaixo serve para deixar em aberto a funcao criada func() mesmo sem nada dentro
# dessa forma ele nao vai executar a excecao, vai executar os prints normal

def func():
	pass

try:
	print 'Primeira linha'
	func()
	print 'Agora nao vai dar erro'
except Exception as e:
	print 'Algo de errado aconteceu'
finally:  ## o finally nao precisa ser sempre colocado, pode ser usado para fechar conexao com servidor
	print 'sempre executa'











