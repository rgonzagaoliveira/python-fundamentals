# SQL ALCHEMY


## criando conexao com o banco

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db')  ## a base esta no banco, neste endereco, com sqlite
# engine = create_engine('postgresql://postgres:123456@localhost:5432/projeto') se quiser fazer o banco com postgres
Base = declarative_base()

## Criando classe Usuario

class Usuario(Base):						### todas as classes tem que herdar a base
	__tablename__ = 'usuarios'   			### tabela de nome usuarios
	id = Column(Integer, primary_key=True)	### criando coluna de Id, inteira e chave primario
	nome = Column(String, nullable=False)	### criando coluna de nome, sendo esta string, nullable nao deixa ser vazio



## O comando abaixo protege o restante do codigo para rodar so que esta abaixo do if...caso o arquivo seja 
# chamado na linha de comando dai ele roda tudo
if __name__ == '__main__':
	Base.metadata.create_all(engine)
	Session = sessionmaker()				## funciona igual ao cur....abre uma sessao
	Session.configure(bind=engine)
	session = Session()
	


	try:

		lista = ['Renato', 'Gabriel', 'Nicia']
		for i in lista:
			usuario = Usuario(nome=i)	## esse comando cria o objeto, dai o alchemy entende que precisa inserir no atribut
			session.add(usuario)		## esse comando diz que e para inserir o usuario, que foi definido na linha de cima
			session.commit()

		users = session.query(Usuario).all()

		for i in users:
			print i.nome, i.id								
		# print session.query(Usuario).filter_by(id=1, nome='Renato').first() 	### esse comando serve para buscar, como se fosse o SELECT
		# print session.query(Usuario).filter_by(id=1).all()
		# session.delete(usuario)					## para deletar, precisa ter o objeto preenchido, como na linha
		# session.commit()						## acima tem a definicao do usuario, ele ja sabe quem tem que deletar

	except Exception as e:
		print e
		session.rollback()
