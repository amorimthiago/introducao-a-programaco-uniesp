#Desenvolva os algoritmos abaixo em linguagem Python. Utilize o VS Code ou Pycharm, mas ao final entregue ao professor um arquivo .py para cada questão desenvolvida. As atividades deverão ser entregues no Github.

#Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
#Imprima o resultado da soma de todos os valores da matriz no terminal;
#E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

import random
import numpy as np
import time
matrizA = []
n = int(input("Informe a quantidade de linhas\n da matriz 1:" ))
m = int(input("Informe a quantidade de colunas\n da matriz 1:" ))
for i in range(n):
     matrizA.append([])
     for j in range(m):
        matrizA[i].append(random.randint(0,100))

for i in range(len(matrizA)):
    for j in range(len(matrizA[i])):
        print(matrizA[i][j], end=" ")
    print ("\n")
soma = []
soma.append(matrizA)
print('='*50)
print(f'A soma de todos os valores da matriz é: {np.sum(soma)}')
print('='*50)
print('='*0)

matrizB= matrizA[:]
print('Matriz sendo multiplicada por 3, aguarde...')
time.sleep(3)
print('='*50)

for linhas in matrizB:
    for colunas in linhas:
        print(colunas*3,end=' ')
    print()