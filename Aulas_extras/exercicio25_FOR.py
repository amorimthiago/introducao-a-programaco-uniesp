# Desenvolver um algoritmo que efetue a soma
#de todos os números ímpares que são múltiplos de três e
#que se encontram no conjunto dos números de 1 até 500.

controle = 0
acumulador = 0

for controle in range(1, 501, 1): # o que esta dentro de range, o primeiro é de onde começa o segundo de onde termina e o terceiro quanto vai pular.
    if (controle % 3) == 0 and (controle % 2) != 0:
   # print(f'O Valor somado para a soma foi {controle}')
     acumulador = acumulador + controle
print(f'A soma dos números impares até 500 é: {acumulador}')