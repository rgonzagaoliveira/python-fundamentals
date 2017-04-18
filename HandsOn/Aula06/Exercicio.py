# ---- CONEXAO COM O BANCO

import psycopg2

# abre a conexao
con = psycopg2.connect(
	'host=%s dbname=%s user=%s password=%s' % (
	'localhost', 'projeto', 'postgres', '123456'
	)
)

print con



## INSERIR UM TITULO - QUE O USUARIO QUISER

# abre a secao

tit = raw_input('Insira o titulo: ')
cont = raw_input('Insira o conteudo: ')


cur = con.cursor()
cur.execute("\
	INSERT INTO posts(conteudo, titulo)\
	VALUES( '%s', '%s')" % (cont, tit))

# comitar os dados
if cur.rowcount:
	print 'Registro inserido com sucesso!'

con.commit()


### USUARIO FAZ UM BUSCA

trecho= raw_input('Insira o conteudo: ')
# cont = raw_input('Insira o conteudo: ')

cur = con.cursor()
cur.execute("SELECT * FROM posts WHERE conteudo LIKE '%%%s%%'" % trecho)

for row in cur.fetchall():
	print "ID %s | Titulo %s | Conteudo %s" % (
		row[0], row[1], row[2]
	)
