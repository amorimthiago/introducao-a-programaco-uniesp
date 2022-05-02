#PROGRAMA QUADRADO 2.0 – O usuário informa três números inteiros, o programa soma esses três valores e depois mostra o quadrado do resultado obtido.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o Terceiro numero: '))
result = n1 + n2 + n3 
quadrado = result **2
print(f'O quadrado do valor dos 3 números é: {quadrado}')