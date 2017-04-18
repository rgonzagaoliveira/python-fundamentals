
# SQL ALCHEMY


## criando conexao com o banco

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db')  ## a base esta no banco, neste endereco
Base = declarative_base()

## Criando classe Usuario

class Usuario(Base):						### todas as classes tem que herdar a base
	__tablename__ = 'usuarios'   			### tabela de nome usuarios
	id = Column(Integer, primary_key=True)	### criando coluna de Id, inteira e chave primario
	nome = Column(String)					### criando coluna de nome, sendo esta string


## O comando abaixo protege o restante do codigo para rodar so que esta abaixo do if...caso o arquivo seja 
# chamado na linha de comando dai ele roda tudo
if __name__ == '__main__':
	Base.metadata.create_all(engine)
	Session = sessionmaker()				## funciona igual ao cur....abre uma sessao
	Session.configure(bind=engine)
	session = Session()
	try:
		# usuario = Usuario(nome='Renato')		## esse comando cria o objeto, dai o alchemy entende que precisa inserir no atributo
		# session.add(usuario)					## esse comando diz que e para inserir o usuario, que foi definido na linha de cima
		# session.commit()
		usuario = session.query(Usuario).get(1)								 	### SELECT - o get utiliza sempre o id para buscar, entre parenteses coloca qual o id vc quer buscar
		# print session.query(Usuario).filter_by(id=1, nome='Renato').first() 	### esse comando serve para buscar, como se fosse o SELECT
		# print session.query(Usuario).filter_by(id=1).all()
		print usuario.nome
		session.delete(usuario)					## para deletar, precisa ter o objeto preenchido, como na linha
		session.commit()						## acima tem a definicao do usuario, ele ja sabe quem tem que deletar

	except Exception as e:
		print session.rollback()

