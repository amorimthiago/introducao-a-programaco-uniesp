# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

compradas = int(input('Digita o numero de maçãs compradas: '))
if compradas >= 12:
    val = compradas *1
else: 
    compradas < 12
    val = compradas *1.30
print(f'Sua compra foi de {compradas} maçãs, que custaram {val} Reais.')