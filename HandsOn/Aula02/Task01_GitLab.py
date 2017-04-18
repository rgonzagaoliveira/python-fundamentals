'''
Na Aula 02 voce aprendeu o conceito de listas.

Abra o script de autenticacao feito na aula01 e o modifique:

Agora voce deve criar um looping infinito e nele deve aparecer um menu informando as opcoes: 
1 - Cadastrar usuario 
2 - acessar sistema 
3 - Sair do Sistema

O script so deve parar caso o usuario digite a opcao 3 que sera equivalente a sair.

Na opcao cadastrar o administrador do sistema deve informar o login que sera cadastrado em uma lista 
e a senha do usuario deve ser cadastrada em uma lista diferente e ambos devem estar no mesmo indice.

Agora o seu sistema de autenticacao deve percorrer a lista e encontrar um usuario, se encontrar o 
usuario ele deve acessar o mesmo indice na outra lista e verificar a senha, caso a senha informada 
seja igual a senha cadastrada na lista, sera liberado o acesso do usuario, caso contrario deve informar: 
Senha nao confere, e caso o usuario nao seja encontrado na lista, deve informar: 
Usuario nao encontrado.

Dica: Lembre-se que voce pode percorrer uma lista com o for a in lista: 
porem para saber o indice da lista voce precisara usar a funcao enumerate.
'''
### Criando um menu

menu = '''
-= SISTEMA =-

1) Cadastrar usuario
2) Acessar sistema
3) Sair

Selecione uma opcao: '''

# Criando a listas vazias
usuarios = []
senhas = []


# Criando um loop infinito

while True:
	banner = input(menu)    # input e igual raw_input porem so aceita inteiro, banner e o nome da variavel


	if banner == 1:
		login = raw_input('Cadastre o login: ')
		senha = raw_input('Cadastre a senha: ')

		usuarios.append(login) ### inserindo o login na lista usuarios
		senhas.append(senha)   ### inserindo a senha na lista senhas

	elif banner == 2:
		login = raw_input('Informe o login: ')
		senha = raw_input('Informe a senha: ')

		if login in usuarios:   # testa se o login informado consta na lista usuario
			if senhas[usuarios.index(login)] == senha:
				print 'Logado com sucesso!'
				continue

		print 'Login ou senha invalidos'

	elif banner == 3:
		print 'Volte Sempre'
		break




