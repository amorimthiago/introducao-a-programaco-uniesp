#Crie um programa em Python que pergunte o nome do usuário e imprima um bom 
# dia com o nome do usuário. Dica: você pode utilizar o método .format() 
# ou uma concatenação de string, por exemplo.

nome = input('Digite o seu nome: ')
print('Bom dia, {}'.format(nome))

#sem .format
mensagem = 'Bom dia2, ' + nome
print(mensagem)