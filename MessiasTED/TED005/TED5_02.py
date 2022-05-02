#Desenvolva um sistema de autenticação, no qual se verifica o login e a senha. O usuário deverá digitar o seu nome de usuário e sua senha. Se os dois valores estiverem correto, imprima uma mensagem de boas-vindas para para o usuário, se não imprima que o login ou a senha estão incorretos. Utilize nome de usuário e senhas fictícias dentro da estrutura de seleção.

print('LOGIN E SENHA DO USUARIO')
login = 'Messias'
senha = '123mudar'
login_digitado = input('Digite o seu nome de usuario: ')
senha_digitado = input('Digite a sua senha: ')
if login_digitado == login and senha_digitado == senha:
    print('voce pode entrar')
else:
    print('Usuario ou senha incorretos, tente novamente')