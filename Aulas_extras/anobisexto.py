
ano = int(input('Digite o ano escolhido: '))

# Verificando se o ano é Bissexto
while ano > 1:

    if (ano % 4) == 0 and (ano % 100) == 0 and (ano % 400) == 0:
     print('O ano é bissexto!')
    elif (ano % 4) != 0:
     print('O ano não é bissexto!')
    elif (ano % 4) == 0 and (ano % 100) != 0:
     print('O ano é bissexto!')
    elif (ano % 4) == 0 and (ano % 100) == 0 and (ano % 400) != 0:
     print('O ano não é bissexto!')

    ano = int(input('Digite o ano escolhido: '))
