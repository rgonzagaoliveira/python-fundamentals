string = 'Python'

print string[3]

print string[:3]

print string[3:]

print string[-3]

#------------------------------------------------
# AO INVES DE USAR HOST, USUARIO E SENHA FIXOS, PODE USAR O RAW IMPUT PARA QUE SEJA INSERIDO

host = '192.168.202.4'

user = 'root'

senha = 1234


# RAW IMPUT ------------------------------------------------
# Voce pode solicitar para o usuario pedir o usuario a senha caso isso altere sempre
# NA VERSAO 3 O NOME DO RAW INPUT E SOMENTE INPUT

host = raw_input('Insira o hostname: ') # solicitando para entrar com o host

user = raw_input('Insira o usuario: ')

senha = raw_input('Insira a senha: ')

print 'Acessando host %s:%s %s' % (user, host, senha) 


# OPERADORES ---------------------------------------------------------------

num1 = int(raw_input('Insira o primeiro valor: ')) # o int esta convertendo a string do raw input em inteiros para poder fazer a conta
num2 = int(raw_input('Insira o segundo valor: '))
	
print num1 * num2
print num1 + num2
print num1 - num2
print num1 / num2
print num1 % num2
print (num1 * num2) + 5

# FORMAS ABREVIADAS DOS OPERADORES-------------------------------------------

numero = 5
numero = numero + 3

# OU

numero += 3 # isso representa a mesma coisa que esta acima

# OPERADORES RELACIONAIS ----------------------------------------------------

# ==
# != ou <>
# < ou <=
# > ou >=
# is  compara booleano

# OPERADORES LOGICOS --------------------------------------------------------

a = 'a'
b = 'b'


# AND
if a == 'a' and b == 'a':
	print 'Verdadeiro'
else:
	print 'Falso'

# OR
if a == 'a' or b == 'a':
	print 'Verdadeiro'
else:
	print 'Falso'

# NOT
if a == 'a' and not b == 'a':
	print 'Verdadeiro'
else:
	print 'Falso'


# CONDICIONAIS ------------------------------------------------------------

nome = raw_input('Informe o sistema operacional: ')

if nome == 'Linux':
	print 'Melhor S.O. de Todos'
elif nome == 'Windows':        # elif e igual ao elseif --- e para adicionar condicoes, quantas quiser
	print 'Bom pra jogar'
elif nome == 'IOS':
	print 'Playboy'
else: 
	print 'Informacao errada, acho que e Android'


# EXERCICIO ---------------------------------------------------------------

# PERGUNTAR A IDADE
# PERGUNTAR SE ESTA ALCOOLIZADO
# PERGUNTAR SE TEM HABILITACAO

idade = int(raw_input('Informe sua idade: '))
alcoolizado = raw_input('Esta alcoolizado? (s/n): ').upper() # transforma sempre em maiscula o que o usuario digita
habilitacao = raw_input('Possui habilitacao? (s/n): ').upper()

# um metodo:

if idade < 18 or alcoolizado == 'S' or habilitacao == 'N':
	print 'Voce nao pode prosseguir'
elif idade >= 18 and alcoolizado == 'N' and habilitacao == 'S':
	print 'Ok, pode prosseguir'
else:
	print 'Voce nao pode prosseguir'


# Outro metodo ----------

if idade >= 18:
	if alcoolizado == 'N':
		if habilitacao == 'S':
			print 'Ok, pode prosseguir'
		else:
 			print 'Voce nao pode prosseguir'
 	else:
		print 'Voce nao pode prosseguir'
else:
	print 'Voce nao pode prosseguir'

# WHILE --- LACOS DE REPETICAO ---------------------------------

i = 0

while i <10:
	print i
	i += 1


# Inserindo condicao para encerrar o while
while i <10:
	if i == 5:
		break
	print i
	i += 1

# Inserindo condicao para pular para o proximo while
while i <10:
	if i == 5:
		i += 1
		continue # para nao executar as linha de baixo e ir direto para o proximo loop (nesse caso ele incremeta mais um, mas nao printa o 5....os demais ele vai printar)
	print i
	i += 1


# FOR ---- Varre a lista ate acabar, cada vez que ele roda, ele assume um valor diferente dentro da lista


for value in ['pera', 'uva', 'banana']:
	if value == 'uva':
		continue # o continue faz pular a uva na hora de printar
	print value
#else: # e colocar o else no for, ele executa tudo que tem dentro do for e depois sempre executa o else

for value in 'PYTHON':
	print value



# LISTAS -------------------------------------------------------

animais = ['gato', 'cachorro', 'elefante']
append.animais('boi') # este comando insere o elemento boi na lista animais no final da lista
print animais

animais.insert(1,'tigre') # este comando insere na posicao 1 o elemento tigre, e empurra todos os demais elementos para frente
print animais

animais.remove('gato') # remove o elemento que voce escolher
print animais

animais.pop() # remove sempre o ultimo elemento da lista
print animais

print animais.count('tigre') # quantos elementos tigres tem na lista
print animais

animais.len(animais) # conta quantos elementos tem na lista animais

print animais.index('cachorro')

aniamis.reverse() # inverte a ordem da lista
print animais

# procura na lista animais o elemento tigre
if 'tigre' in animais: 
	print 'Encontrei o tigre'





