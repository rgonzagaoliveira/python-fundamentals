#### Importando #######

from Usuarios.Usuarios import *
from Servidores.Servidores import *



## Fazendo o menu

menu = '''
-= SISTEMA =-

1) Cadastrar usuario
2) Acessar sistema
3) Cadastrar servidor
4) Excluir Servidor
5) Sair

Selecione uma opcao: '''


# Criando um loop infinito

while True:
	banner = input(menu)    # input e igual raw_input porem so aceita inteiro, banner e o nome da variavel

	if banner == 1:
		if inserir_user():
			print 'Usuario cadastrado com sucesso'
		else:
			print 'Falha ao cadastrar'

	elif banner == 2:
		if login_user():
			print 'Logado com sucesso!'
		else:
			print 'Usuario ou senha invalidos'

	if banner == 3:
		if inserir_servidor():
			print 'Servidor cadastrado com sucesso'
		else:
			print 'Falha ao cadastrar'

	elif banner == 4:
		if excluir_servidor():
			print 'Servidor excluido com sucesso'
		else:
			print 'Falha ao excluir'

	elif banner == 5:
		print 'Volte Sempre'
		break



