#### Importando #######

from Usuarios.Usuarios import *
from Servidores.Servidores import *

## Fazendo o menu

menu = '''
-= SISTEMA =-

1) Cadastrar usuario
2) Acessar sistema
3) Sair

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

	elif banner == 3:
		print 'Volte Sempre'
		break



