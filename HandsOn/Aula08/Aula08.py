### USANDO MONGODB ###################################3

# importando

from pymongo import MongoClient

client = MongoClient('127.0.0.1')
db = client['devops']


### INSERINDO - INSERT

db.fila.insert({
	'_id':2,
	'servico': 'intranet',
	'status': 0
})


db.fila.insert({
	'_id':3,
	'servico': 'dns',
	'status': 0
})

### ATUALIZANDO - UPDATE 
# tomar cuidado pode alterar todo o banco se o criterio nao for bem especifico


db.fila.update(
	{'_id': 1},    ### dessa forma ele vai alterar o ID=1
	{'$set': {'status': 1}} ### usa-se o set e depois defini tudo o que vai ser alterado, nesse o status vai ficar 1
)


### REMOVENDO - DELETE

db.fila.remove({'_id': 3})


### PROCURANDO - SELECT

for d in db.fila.find({}):
	print d







