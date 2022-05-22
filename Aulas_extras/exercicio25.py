# Desenvolver um algoritmo que efetue a soma
#de todos os números ímpares que são múltiplos de três e
#que se encontram no conjunto dos números de 1 até 500.

controle = 1
acumulador = 0
while controle <= 250:
  #print(f'Ele esta no ciclo {controle}')

  if (controle % 3) == 0 and (controle % 2) != 0:
    print(f'O Valor somado para a soma foi {controle}')
    acumulador = acumulador + controle

  controle = controle + 1
print(f'~'*50)
print(f'A soma dos impares é: {acumulador}')
print(f'~'*50)
