### PROGRAMACAO ORIENTADA A OBJETOS #####

## Classe
# como se fosse um projeto com as caracteristicas (exemplo, classe projeto de uma casa)
# o init e o construtor
import psycopg2


class Conexao: 
	con = None   ## criando um atributo que pode ser acessado por todos os metodos dentro desta classe
	cur = None	 ## criando um atributo que pode ser acessado por todos os metodos dentro desta classe


# metodo e o que a classe executa, usando a palavra self. antes das variaveis e funcoes significa que
# essa funcao/variavel pode ser usada dentro de outros metodos
	# @staticmethod --- caso seja declarado q o metodo e estatico, nao se utiliza mais o self. para chamar e nem precisa herdar mais
	def conectar(self, host, db, user, passwd):    # o def e o metodo da classe, o self e obrigatorio
		self.con = psycopg2.connect(
			"host=%s dbname=%s user=%s password=%s" %
			(host, db, user, passwd)
		)
		self.cur = self.con.cursor()
		# self.find_one(3) --- uso o self para que ele entenda que a funcao find_one esta em outro metodo. o valor 3 e o id.



### a classe Banco esta herdando todos os atributos e funcoes da classe Conexao
### pode-se fazer herdar de varias classes - heranca multipla
class Banco(Conexao):
	def __init__(self, host, db, user, passwd): # o metodo init e o unico que executa sem ser chamado, pois e o construtor
		self.conectar(host, db, user, passwd)   # o construtor inicia a classe, nesse caso ele constroi a conexao ao chamar a classe conexao
		# self.con, self.cur = Conexao.conectar(host, db, user, passwd) - usa-se isso quando esta usando um metodo estatistico


	def find_one(self, id):
		self.cur.execute("SELECT * FROM posts WHERE id=%s" % id)
		return self.cur.fetchone()



## Objeto
# herda as caracteristicas do projeto (e a casa em si, com as caracteristicas da casa do projeto)

objeto = Banco('localhost', 'projeto', 'postgres', '123456')
print objeto.find_one(2) ## ao printar ele mostra que o objeto e uma instancia da classe Banco
# ta buscando o registro de id 2



# o python permite declarar varias de um vez
a, b, c, d = [1, 2, 3, 'a']
	print a, b, c, d