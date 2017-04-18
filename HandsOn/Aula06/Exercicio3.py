'''
CRIAR A TABELA ABAIXO NO BANCO

CREATE TABLE users (
	id serial primary key,
	usuario VARCHAR(255),
	pass VARCHAR(255)
);

INSERIR UM REGISTRO
INSERT INTO users (usuario, pass) VALUE('RENATO','GONZAGA');
INSERT INTO users (usuario, pass) VALUE('NICIA','GONZAGA');

'''

##### CONECTANDO NO BANCO

import psycopg2

# abre a conexao
con = psycopg2.connect(
	'host=%s dbname=%s user=%s password=%s' % (
	'localhost', 'projeto', 'postgres', '123456'
	)
)

cur = con.cursor()
cur.execute

##### MENU DE SELECAO E LOGIN


session = False
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
		user = raw_input('Insira o usuario: ')
		senha = raw_input('Insira a senha: ')

		query = "SELECT * FROM users WHERE usuario = '%s' and pass = '%s'" % (user, senha)
		cur.execute(query)

		usuario = cur.fetchone()

		if usuario:
			session = True
			print 'Usuario logado com sucesso'
			print 
		else:
			print 'Username ou password invalido'
			print

	elif option == 2:
			if not session:     # verifica se o session e falso
				print 'Usuario nao logado'
				continue  # o continue faz ele ignorar tudo o q esta abaixo do if not session
			print 'Opcao 2 selecionada'
			user = raw_input('Digite o nome: ')
			senha = raw_input('Digite a senha: ')

			query = "INSERT INTO users(usuario, pass) VALUES('%s', '%s')" % (user, senha)
			print query
			try:			## nao comita ate verificar se houve a insercao de usuario
				cur.execute(query)
				if cur.rowcount:    ## conta e verifica se cur for diferente de 0, ele comita
					con.commit()
					print 'Usuario inserido com sucesso'
			except Exception as e:
				con.rollback()     
				print 'Erro ao inserir usuario'
				print
	## se ele nao conseguir executar a query acima, ele retorna o banco ao original

	elif option == 3:
			if not session:
				print 'Usuario nao logado'
				continue

			user = raw_input('Localizar o usuario: ')
			query = "SELECT * FROM users WHERE usuario LIKE '%%%s%%'" % user  ## quando usa o like tem que escapar usando o simbolo %
			cur.execute(query)  # tras o resultado da query

			usuario = cur.fetchone()  ## colocar em usuario o resultado da busca que fetchone fez em cur
			if usuario:
				print '======================='
				print 'Usuario: %s\nSenha: %s' % (usuario[1], usuario[2])
				print '======================='

	elif option == 4:
		print 'Volte Sempre'
		flag = False   ## Aqui pode usar o exit ou o break tambem



