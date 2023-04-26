'''O sistema de login deve permitir que novos usuários sejam cadastrados, e que usuários existentes possam fazer o login. O sistema deve alertar caso a senha e login não estejam corretos.'''

# O sistema de login deve permitir que novos usuários sejam cadastrados

# O sistema não deve permitir que usuários duplicados sejam cadastrados

# O sistema deve permitir que usuários existentes possam fazer o login

# O sistema deve alertar caso a senha e login não estejam corretos

# Processo 01 - O sistema de login deve permitir que novos usuários sejam cadastrados

# Processo 02 - O sistema não deve permitir que usuários duplicados sejam cadastrados

# Processo 03 - Permitir que usuários existentes possam fazer login


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

# Processo 03 - Permitir que usuários existentes possam fazer login
resposta = input('[1] - Cadastrar novo usuário [2] - Fazer login: ')

# if condição == condição | comparação no python
if resposta == '1':
    # abaixo é necessário realizar identamento (espaçamento)
    # armazenando usuários existentes
    usuarios = ['Rafael', 'Metal Omega', 'Silveira']
    senhas = ['12345', 'abcdef', '123abcd']
    # recebendo usuário | em Python digitar sempre em minúsculo e sem caracter especial
    usuario_digitado = input('digite seu usuário: ')
    # recebendo senha
    senha_digitada = input('digite sua senha: ')
    # comando append adiciona variável
    usuarios.append(usuario_digitado)
    senhas.append(senha_digitada)


# elif resposta == '2':
    # Processo 03 - Permitir que usuários existentes possam fazer login
