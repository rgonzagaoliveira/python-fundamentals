#### Separando por funcoes #######


## Fazendo o menu

menu = '''
-= SISTEMA =-

1) Cadastrar usuario
2) Acessar sistema
3) Sair

Selecione uma opcao: '''

# Criando a listas vazias
usuarios = []
senhas = []


def inserir_user():
		global usuarios, senhas ## as variaveis usuarios e senhas estao no escopo global
		login = raw_input('Cadastre o login: ')
		senha = raw_input('Cadastre a senha: ')
		usuarios.append(login) ### inserindo o login na lista usuarios
		senhas.append(senha)   ### inserindo a senha na lista senhas
		return True

def login_user():
		global usuarios, senhas
		login = raw_input('Informe o login: ')
		senha = raw_input('Informe a senha: ')
		
		if login in usuarios:   # testa se o login informado consta na lista usuario
			if senhas[usuarios.index(login)] == senha:
				return True
		return False



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



