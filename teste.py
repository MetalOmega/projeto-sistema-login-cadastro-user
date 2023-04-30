resposta = input('[1] - Cadastrar novo usuário [2] - Fazer login: ')

usuarios = ['Rafael', 'Metal Omega', 'Silveira']
senhas = ['12345', 'abcdef', '123abcd']

if resposta == '1':
    usuario_digitado = input('digite seu usuário: ')
    if usuario_digitado in usuarios:
        print('usuário existente')

    else:
        senha_digitada = input('digite sua senha: ')
        usuarios.append(usuario_digitado)
        senhas.append(senha_digitada)
elif resposta == '2':
    usuario_digitado = input('Digite seu usuário: ')
    senha_digitada = input('Digite sua senha: ')
    encontrado = False
    for indice, usuario in enumerate(usuarios):
        if usuario_digitado == usuario and senha_digitada == senhas[indice]:
            print('Login realizado com sucesso')
            encontrado = True
        elif encontrado == False:
            print('usuário ou senha incorreto!')
else:
    print('digite apenas 1 ou 2')
