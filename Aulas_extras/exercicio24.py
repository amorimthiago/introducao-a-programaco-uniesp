
dia = int(input('Digite o seu dia escolhido: '))
mes = int(input('Digite o mes escolhido: '))
ano = int(input('Digite o ano escolhido: '))

# Verificando se o ano é Bissextp
if (ano % 4) == 0 and (ano % 100) == 0 and (ano % 400) == 0:
  print('O ano é bissexto!')
  b = True
elif (ano % 4) != 0:
  print('O ano não é bissexto!')
  b = False
elif (ano % 4) == 0 and (ano % 100) != 0:
  print('O ano é bissexto!')
  b = True
elif (ano % 4) == 0 and (ano % 100) == 0 and (ano % 400) != 0:
  print('O ano não é bissexto!')
  b = False

if mes == 1 and dia >= 1 and dia <= 31:
    print('Estamos falando do mês de Janeiro')
    if dia >=1 and dia <= 20:
        print('Seu signo é Capricornio')
    else:
        print('Seu signo é Aquário') 

elif mes == 2 and dia >= 1 and dia <= 28 and b == False:
  print('Estamos falando do mês de Fevereiro')
  if dia >= 1 and dia <= 18:
    print('Seu signo é Aquário')
  else:
    print('Seu signo é Peixes')

elif mes == 2 and dia >= 1 and dia <= 29 and b == True:
  print('Estamos falando do mês de Fevereiro')
  if dia >= 1 and dia <= 18:
    print('Seu signo é Aquário')
  else:
    print('Seu signo é Peixes')

elif mes == 3 and dia >= 1 and dia <= 31:
    print('Estamos falando do mês de Março')    
elif mes == 4 and dia >= 1 and dia <= 30:
    print('Estamos falando do mês de Abril')
    
elif mes == 5 and dia >= 1 and dia <= 31:
    print('Estamos falando do mês de Maio')
elif mes == 6 and dia >= 1 and dia <= 30:
    print('Estamos falando do mês de Junho')
elif mes == 7 and dia >= 1 and dia <= 31:
    print('Estamos falando do mês de Julho')
elif mes == 8 and dia >= 1 and dia <= 31:
    print('Estamos falando do mês de Agosto')
elif mes == 9 and dia >= 1 and dia <= 30:
    print('Estamos falando do mês de Setembro')
elif mes == 10 and dia >= 1 and dia <= 31:
    print('Estamos falando do mês de Outubro')
elif mes == 11 and dia >= 1 and dia <= 30:
    print('Estamos falando do mês de Novembro')
elif mes == 12 and dia >= 1 and dia <= 31:
    print('Estamos falando do mês de Dezembro')
    if dia >= 1 and dia <= 21:
      print('Seu signo é Sagitário')
    else:
      print('Seu signo é Capricórnio')
else:
    print('Você não digitou uma data válida')

