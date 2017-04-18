### DATETIME ### Para manipular datas e horarios

from datetime import datetime, timedelta, date, time

# para pegar a data atual
print datetime.now() 

# para formatar a data como quiser
print datetime.now().strftime('%m/%d/%Y') 

print datetime.now().strftime('%d.%m.%y')


# para inserir uma data
print datetime(1985, 11, 18, 04, 51, 0)
print datetime(1985, 11, 18, 04, 51, 0).strftime('%d/%b/%Y') 

# TIMEDELTA -----------------------------------------------------------------------------------------

# Somando um periodo de 5 dias a mais na data atual
print datetime.now() + timedelta(5) # o padrao e dias, mas pode usar todos os parametros abaixo

print datetime.now() + timedelta(weeks=12, days=20, hours=3, minutes=20, seconds=15, milliseconds=50)




# TODAY ## Pega somente a data, desconsiderando o horario

print date.today()



### 

data1 = datetime(1987, 11, 18, 04, 51, 0)
data2 = datetime(1985, 11, 18, 04, 51, 0)

if (data1 - data2).total_seconds() > 3600:
	print 'Seu token expirou'
else:
	print 'Acesso liberado'







