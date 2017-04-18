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

    def insert(self, titulo, conteudo):
        try:
            query = "INSERT INTO posts(titulo, conteudo) \
                    VALUES('%s', '%s')" % (titulo, conteudo)
            self.cur.execute(query)
            print self.cur.lastrowid
            # self.con.commit()
            return True
        except Exception as e:
            raise Exception(e)

    def update(self, titulo, conteudo, id):
        try:
            query = "UPDATE posts SET titulo='%s', conteudo='%s' WHERE id=%s" % (titulo, conteudo, id)
            self.cur.execute(query)
            # self.con.commit()
            return True
        except Exception as e:
            raise Exception(e)

    def delete(self, id):
        try:
            query = "DELETE FROM posts WHERE id=%s" % id
            self.cur.execute(query)
            # self.con.commit()
            return True
        except Exception as e:
            raise Exception(e)


objeto = Banco('localhost', 'projeto', 'postgres', '123456')

try:
    objeto.insert(titulo='Meu titulo', conteudo="Meu conteudo")
    objeto.update(titulo='Novo titulo', conteudo="Novo conteudo", id=2)
    objeto.delete(id=2)
except Exception as e:
    print 'Falha: %s' % e