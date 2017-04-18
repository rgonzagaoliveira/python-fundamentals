import psycopg2


class Conexao:
    @staticmethod
    def conectar(host, dbname, user, passwd):
        con = psycopg2.connect(
            "host=%s dbname=%s user=%s password=%s" %
            (host, dbname, user, passwd)
        )
        cur = con.cursor()
        return con, cur


class Banco:
    con = None
    cur = None

    def __init__(self, host, dbname, user, passwd):
        self.con, self.cur = Conexao.conectar(host, dbname, user, passwd)

    def find_one(self, id):
        self.cur.execute("SELECT * FROM posts WHERE id=%s" % id)
        return self.cur.fetchone()

    def insert(self, **kwargs):
        tabela = kwargs['tabela']
        del kwargs['tabela']
        campos = kwargs.keys()
        campos = ','.join(campos)
        values = ["'%s'" % string for string in kwargs.values()]
        values = ','.join(values)

        try:
            query = "INSERT INTO %s(%s) \
            VALUES(%s)" % (tabela, campos, values)
            self.cur.execute(query)
            self.con.commit()
            return True
        except Exception as e:
            self.con.rollback()
            return False


objeto = Banco('localhost', 'projeto', 'postgres', '123456')
# resultado = objeto.insert(tabela='posts', titulo='Meu titulo', conteudo="Meu conteudo")
objeto.insert(tabela='posts', titulo='Meu titulo', conteudo="Meu conteudo")
# if resultado:
#     print 'adicionado com sucesso'
# else:
#     print 'falha ao adicionar'A')




