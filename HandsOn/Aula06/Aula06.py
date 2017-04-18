### Importando o SQL

import psycopg2

# abre a conexao
con = psycopg2.connect(
	'host=%s dbname=%s user=%s password=%s' % (
	'localhost', 'projeto', 'postgres', '123456'
	)
)

# abre a secao
cur = con.cursor()

## como inserir dados na tabela ----------------
# executando os comandos na secao
cur.execute("\
	INSERT INTO posts(conteudo, titulo)\
	VALUES('bla bla bla bla bla bla' , 'A crise no Brasil')")

# comitar os dados
if cur.rowcount:
	print 'Registro inserido com sucesso!'
	con.commit()

### Como consultar o banco - SELECT ----------

cur = con.cursor()

cur.execute('SELECT * FROM posts')

# fetchall mostra todos os resultados do select
# fetchone mostra somente um registro

for row in cur.fetchall():
	print 'ID: %s \nTitulo: %s\n Conteudo: %s' % (
		row[0], row[1], row[2]
)


row = cur.fetchone():
print 'ID: %s \nTitulo: %\n Conteudo: %' % (
	row[0], row[1], row[2]
)

#### Fazendo INSERT, UPDATE, DELETE
# usa-se o try para que caso esteja realizando varios comandos no banco e apenas um de errado
# ele trata a excessao dando um rollback em tudo e voltando tudo ao original

try:
	cur.execute(" \
	INSERT INTO posts(conteudo, titulo)\
	VALUES('%s', '%s')" % ('Meu conteudo', 'Titulo'))

	if cur.rowcount:
		print 'Registro inserido com sucesso!'
		con.commit()

except Exception as e:
	print e
	con.rollback()





