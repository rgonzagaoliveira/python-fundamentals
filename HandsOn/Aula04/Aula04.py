#### IMPORTANDO MODULOS ####

### MODULO PARAMARIKO #### Para conectar com servidores

from paramiko.client import SSHClient # Importando submodulos Clinte
import paramiko # importando paramiko, embora nao importe os submodulos



client = SSHClient() # declarando uma classe

# carregando certificados do servidor
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = '192.168.202.4'
user = 'noturno'
password = '4linux'

# conectar (se estiver usando usuario e senha precisa colocar hostname, usuario e senha)

client.connect(hostname=host, username=user, password=password)
stdin, stdout, stderr = client.exec_command('ls -la')

print stdout.read()



# para verificar os erros de comando caso ocorram - se quiser testar basta digitar um comando errado na linha acima do exec.command
if stderr.channel.recv_exit_status() != 0:
	print stderr.channel.recv_exit_status()
	print stderr.read()
else:
	print stdout.read()



