#### USANDO O MYSQL

import MySQLdb

con = MySQLdb.connect(
	host='127.0.0.1', user='admin', passwd='-Renato14', db='projeto'
)

print con # para verificar se a conexao teve sucesso

cur = con.cursor()


## INSERT
try:
	cur.execute(
		"INSERT INTO posts(titulo, conteudo) VALUES('Meu titulo', 'Meu conteudo')"
	)
	con.commit()

except Exception as e:
	con.rollback()

## UPDATE
try:
	cur.execute(
		"UPDATE posts SET titulo='Novo titulo' WHERE id=2"
	)
	con.commit()
except Exception as e:
	con.rollback()

## SELECT
# selecionando apenas o id 1, usar o fetchone
cur.execute('SELECT * FROM posts WHERE id=2'
)
print cur.fetchone()


# selecionando todos os posts, usar fetchall
cur.execute(
	'SELECT * FROM posts'
)

for row in cur.fetchall():
	print row

# fechar a sessao
cur.close()

# fechar a conexao
con.close()
