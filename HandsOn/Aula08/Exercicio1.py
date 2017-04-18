
from pymongo import MongoClient

client = MongoClient('localhost')
db = client['aula']

session = False

while True:
    banner = '''Menu:
1) Logar
2) Cadastrar usuario
3) Lista usuario
4) Sair
Selecione a opcao: '''

    option = int(raw_input(banner))

    if option == 1:
        user = raw_input('Username: ')
        pswd = raw_input('Password: ')

        result = db.sistema.find({
            "usuario": user,
            "senha": pswd
        }).limit(1)

        if result.count() != 0:
            print "Logado com sucesso"
            session = True
        else:
            print "Usuario ou senha invalidos"
    elif option == 2:
        if not session:
            print 'Usuario nao logado'
            continue

        user = raw_input('Novo username: ')
        pswd = raw_input('Novo password: ')

        db.sistema.insert({
            "usuario": user,
            "senha": pswd
        })
        print "Inserido com sucesso"
    elif option == 3:
        if not session:
            print 'Usuario nao logado'
            continue
        user = raw_input('Localizar usuario: ')

        result = db.sistema.find({
            "usuario": user
        })

        if result.count() != 0:
            print '===================='
            print 'Usuario: %s\nSenha: %s' % (result[0]['usuario'], result[0]['senha'])
            print '===================='

    elif option == 4:
        print 'Volte sempre'
        exit()