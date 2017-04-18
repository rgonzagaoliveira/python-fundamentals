'''
Precisamos de um sistema que mostre quem é o usuário que acabou de se logar no sistema.

Para fazer isso você precisa criar um script em python, que receba o login e a senha de um determinado usuário, 
e mostre na tela:

Seja Bem Vindo [Usuario].

Dica: Para fazer esse script você precisará de duas variáveis e utilizar dos comandos raw_input e print.
'''


user = raw_input('Insira o usuario: ')
pswd = raw_input('Insira sua senha: ')

print 'Seja Bem Vindo %s' % user