#!/usr/bin/python
   
import psycopg2

# abre a conexao
con = psycopg2.connect(
    'host=%s dbname=%s user=%s password=%s' % (
    'localhost', 'dexter', 'postgres', '123456'
    )
)
# abre a secao
cur = con.cursor()

## Definindo funcoes de inserir usuario e logar
def inserir_servidor():
    nome = raw_input('Cadastre o nome: ')
    ip = raw_input('Cadastre o IP: ')
    admin = raw_input('Cadastre o Administrador: ')
    global cur, con
    
    try:    
        cur.execute("INSERT INTO servidores (nome, ip, administrador) VALUES('%s', '%s', '%s')" % (nome, ip, admin))
        # comitar os dados
        if cur.rowcount:
            con.commit()
            return True
    except Exception as e:
        con.rollback()
        return False



def excluir_servidor():
    ip = raw_input('Informe o ip: ')
    global cur, con
    
    try:
        cur.execute("DELETE FROM servidores WHERE ip = '%s'" % ip)
        # comitar os dados
        if cur.rowcount:
            con.commit()
            return True
    except Exception as e:
        con.rollback()
        return False






# import os
# import json
# import psycopg2

# def cadastrar_servidor():
#     try:
#         con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=123456")
#         cur = con.cursor()
#         servidor = {}
#         servidor["endereco"] = raw_input("Digite o endereco de ip do servidor: ")
#         servidor["nome"] = raw_input("Digite o nome desse servidor: ")
#         servidor["administrador"] = raw_input("Digite o administrador: ")
#         cur.execute("insert into servidores(nome,endereco_ip,administrator)\
#                      values('%s','%s','%s')"%(
#                             servidor['nome'],servidor['endereco'],servidor['administrador'])
#                    )
#         con.commit()
#         print "Cadastrado com sucesso!!!"
#     except Exception as e:
#         print "Falhou ao conectar com o banco %s"%e
#         con.rollback()
#     finally:
#         cur.close()
#         con.close()

 

# def remover_servidor():
#     try:
#         con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=123456")
#         cur = con.cursor()
#         cur.execute("select * from servidores")
#         for s in cur.fetchall():
#             print "%s - %s"%(s[0],s[1])
#         srv = input("Digite o numero do servidor que voce quer remover: ")
#         cur.execute("delete from servidores where id=%s"%srv)
#         con.commit()
#         print "Servidor removido com sucesso!"
#     finally:
#         cur.close()
#         con.close()

# def definir_administrador():
#     try:
#         con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=123456")
#         cur = con.cursor()
#         cur.execute("select * from servidores")
#         for s in cur.fetchall():
#             print "%s - %s Administrador Atual[%s]"%(s[0],s[1],s[3])
#         srv = input("Digite o numero do servidor que voce quer definir o administrador: ")
#         admin = raw_input("Digite o email do administrador desse servidor:")
#         cur.execute("update servidores set administrator='%s' where id=%s"%(admin,srv))
#         con.commit()
#         print "Administrador definido com sucesso!"
#     except Exception as e:
#         print "Falhou! %s"%e
#     finally:
#         cur.close()
        # con.close()

