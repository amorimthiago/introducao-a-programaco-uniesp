# Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

import time
numeros = list(range(21))
print(f'=' * 35)
print('Leitura do Números') 
print(f'=' * 35)
print(numeros)
print(f'=' * 35)
time.sleep(2)
print('Ordem descrescente') 
print(f'=' * 35)
decrescente = list(range(20, -1, -1))
print(decrescente)
time.sleep(1.5)
print(f'=' * 35)
print('Ordem decrescente realizada com sucesso!')
print(f'=' * 35)
