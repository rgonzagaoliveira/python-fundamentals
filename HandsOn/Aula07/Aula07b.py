# SQL ALCHEMY


## criando conexao com o banco

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///banco.db')  ## a base esta no banco, neste endereco, com sqlite
# engine = create_engine('postgresql://postgres:123456@localhost:5432/projeto') se quiser fazer o banco com postgres
Base = declarative_base()


class Funcionario(Base):
	__tablename__ = 'funcionario'
	id = Column(Integer, primary_key=True)
	nome = Column(String)

	dependentes = relationship('Dependentes') ### referencia do SQL alchemy, ele sabe que tem que buscar da classe dependentes a informacao


class Dependentes(Base):
	__tablename__ = 'dependentes'
	id = Column(Integer, primary_key=True)
	nome = Column(String)

	funcionario_id = Column(Integer, ForeignKey('funcionario.id'))

if __name__ == '__main__':
	Base.metadata.create_all(engine)
	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()

	try:
		funcionario = Funcionario(id=1, nome='Nicia Gonzaga')
		session.add(funcionario)

		dependente1 = Dependentes(id=1, nome='Renato')
		dependente2 = Dependentes(id=2, nome='Tico')

		funcionario.dependentes.append(dependente1)  ### o append adiciona o dependente dentro da lista de dependentes
		funcionario.dependentes.append(dependente2)

		session.add(dependente1)
		session.add(dependente2)
		session.commit()

	except Exception as e:
		print e
		session.rollback()





