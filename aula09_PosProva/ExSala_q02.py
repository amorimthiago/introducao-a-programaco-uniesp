# Faça um programa que mostre as tabuadas dos números de 1 a 10.

for multiplicador in range(0, 11):
   
    print(f'Tabuada do {multiplicador} -------')

    for multiplicando in range(0, 11):
       
       resultado = multiplicador * multiplicando
       
       print(str(multiplicador) + 'x' + str(multiplicando) + ' = ' + str(resultado))