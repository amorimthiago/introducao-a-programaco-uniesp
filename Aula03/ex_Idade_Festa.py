idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('Pode entrar na Festa!')
elif idade >= 16 and idade <= 17:
    print('É hora de voltar para a sua casa')
else:
    print('Vou chamar seus pais.')