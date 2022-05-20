#Pergunte o nome e idade de pessoas, coloque em um dicionario e imprima eles separadamente:
'''
dados = dict()
lista = list()
for c in range(0, 3):
    dados['nome'] = str(input('Digite o nome: '))
    dados['idade'] = int(input('Digite a idade: '))
    lista.append(dados.copy())
for e in lista:
    for k, v in e.items():
        print(f'Meu amigo {k} tem {v} anos.')
'''
n = int(input('Numeros de cadastros: '))
d = {}
for i in range(n):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    d.update({nome:idade})
for k, v in d.items():# k é a Key(primeiro elemento e V é o value o segundo elemento)
    print(f'=' * 55)
    print(f'=' * 55)
    print(f'Seu nome é {k} e sua idade é {v} anos.' )
print(f'=' * 55)