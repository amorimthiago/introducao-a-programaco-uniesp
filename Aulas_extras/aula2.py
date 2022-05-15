#exemplo de IF e Else
'''
name = input("Digite o seu nome: ")
if name == 'Alice':
    print('Hi Alice')

#exemplo de IF e Else
name = input("Digite o seu nome: ")
if name == 'Alice':
    print('Hi Alice')
else:
    print('Você não é Alice')

#exemplo de IF elif e Else
# se o primeiro for conseguido termina as respostas.
name = input("Digite o seu nome: ")
idade = input('Digite a sua idade')
if name == 'Alice':
    print('Hi Alice')
elif idade < 12:
    print('Você não é Alice')    
else:
    print('Você não é Alice')
'''
#
name = str(input("Digite o seu nome: "))
idade = int(input('Digite a sua idade: '))
if name.upper() == 'Alice'.upper() and idade > 12:
  print('Oi Alice, você tem mais de 12 anos')
elif name != 'Alice':
    print('Você não é Alice, ou tem menos de 12 anos')
else:
  print('Alice você tem menos de 12 anos')