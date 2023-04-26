'''O sistema de login deve permitir que novos usuários sejam cadastrados, e que usuários existentes possam fazer o login. O sistema deve alertar caso a senha e login não estejam corretos.'''

# O sistema de login deve permitir que novos usuários sejam cadastrados

# O sistema não deve permitir que usuários duplicados sejam cadastrados

# O sistema deve permitir que usuários existentes possam fazer o login

# O sistema deve alertar caso a senha e login não estejam corretos

# Processo 01 - O sistema de login deve permitir que novos usuários sejam cadastrados

'''
 1 - Quais são os dados de entrada necessários?
   - usuario, senha
 2 - O que devo fazer com estes dados?
   - registrar usuário e senha digitados
 3 - Quais são as restrições deste problema?
   - não deve permitir cadastro de usuários já existentes
 4 - Qual é o resultado esperado?
   - um novo usuário e senha cadastrados
 5 - Qual é a sequência de passos necessários para chegar ao resultado final?
   - receber o usuário
   - receber a senha
   - verificar se o usuário já existe
   - caso não exista, cadastrar aquele usuário e senha
'''
# armazenando usuários existentes

usuarios = ['Rafael', 'Metal Omega', 'Silveira']
senhas = ['12345', 'abcdef', '123abcd']

# recebendo usuário
usuario = input('digite seu usuário: ')

# recebendo senha
senha = input('digite sua senha: ')

# verificar usuários existentes
for usuario in usuarios:
    print(usuario)
