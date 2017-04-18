
'''
CRIE UM MENU COM 4 OPCOES, SOMENTE SE SELECIONAR A QUARTA OPCAO O PROGRAMA DEVERA ENCERRAR

'''


flag = True

while flag:
	banner = '''Menu:

1-Logar
2-Inserir Usuario
3-Buscar Usuario
4-Sair

Selecione a opcao: '''

	option = int(raw_input(banner))

	if option == 1:
		print 'Opcao 1 selecionada'
	elif option == 2:
		print 'Opcao 2 selecionada'
	elif option == 3:
		print 'Opcao 3 selecionada'
	elif option == 4:
		print 'Volte Sempre'
		flag = False   ## Aqui pode usar o exit ou o break tambem