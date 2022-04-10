#Crie um programa para verificar se a média aritmética de uma disciplina atingiu a nota 7,0. Considere três notas, e aplique a fórmula da média aritmética, se o aluno atingiu a nota mínima ou maior, imprima uma mensagem de parabéns, se não uma mensagem de que ele precisa estudar um pouco mais.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceitanota: '))
media = (nota1 + nota2 + nota3) / 3 
print(f'A media das 3 notas é {media}')
if media <7:
    print('Você precisa estudar um pouco mais.')
else: 
    print('Parabens você passou de ano. ')

