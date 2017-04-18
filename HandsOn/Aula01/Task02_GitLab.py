'''
Agora que voce ja fez um sistema de login basico, so sera possivel fazer a autenticacao de usuarios 
previamente definidos no nosso sistema.

Para isso precisamos ter duas variaveis que vao armazenar um usuario e uma senha especificadas pelo programador. 
Por exemplo: usuario = arthur.dent senha = mochileiro

Se o usuario informado for igual ao usuario especificado no sistema e a senha desse usuario for igual a senha 
especificada no sistema. Aparecera a mensagem:

Usuario Autenticado com Sucesso!

Seja Bem Vindo [Usuario]

Caso constrario aparecera:

Acesso Negado

'''

user = raw_input('Insira o usuario: ')
pswd = raw_input('Insira sua senha: ')

usuario = 'arthur.dent'
senha = 'mochileiro'

if user == usuario and pswd == senha:
	print 'Seja Bem Vindo %s' % user
else:
	print 'Acesso Negado'