#!/usr/bin/python

# Criando a listas vazias
usuarios = []
senhas = []

## Definindo funcoes de inserir usuario e logar
def inserir_user():
        global usuarios, senhas ## as variaveis usuarios e senhas estao no escopo global
        login = raw_input('Cadastre o login: ')
        senha = raw_input('Cadastre a senha: ')
        usuarios.append(login) ### inserindo o login na lista usuarios
        senhas.append(senha)   ### inserindo a senha na lista senhas
        return True

def login_user():
        global usuarios, senhas
        login = raw_input('Informe o login: ')
        senha = raw_input('Informe a senha: ')
        
        if login in usuarios:   # testa se o login informado consta na lista usuario
            if senhas[usuarios.index(login)] == senha:
                return True
        return False







# def cadastrar_usuario(): 
#     usuarios = []   
#     if not os.stat("banco.json").st_size == 0:
#         with open("banco.json","r") as f:
#             dicionario_usuarios = json.load(f)
#         usuarios = dicionario_usuarios["usuarios"]
#         dicionario_usuarios["usuarios"] = usuarios
#     else:
#         dicionario_usuarios = {"usuarios":usuarios}

#     usuario = {"login":"","senha":""}
#     usuario["login"] = raw_input("Digite o login do usuario: ")
#     usuario["senha"] = raw_input("Digite a senha do usuario: ")
#     usuarios.append(usuario)

#     try:
#         with open("banco.json","w") as f:
#             json.dump(dicionario_usuarios,f)
#     except Exception as e:
#         print "Falhou ao escrever no arquivo %s"%e

# def acessar_sistema():
#     if not os.stat("banco.json").st_size == 0:
#             with open("banco.json","r") as f:
#                 dicionario_usuarios = json.load(f)

#     print "-= Sistema de Autenticao =-"
#     login = raw_input("Digite o login do usuario: ")
#     senha = raw_input("Digite a senha do usuario: ")
    
#     for u in dicionario_usuarios["usuarios"]:
#         if u["login"] == login and u["senha"] == senha:
#             print "Usuario Autenticado com Sucesso"
#             break        
#     else:
#         print "Usuario nao encontrado" 


