from time import sleep
glossário = {'Python':' uma linguagem de programação','HTML':' Linguagem de marcação para web','Linux':' um sistema operacional',
'Google Colab':'Programa On-line do google para usar o python, baseado no Jupiter','Visual Studio Code':'Programa gratuito para usar liguagens de programação e web'}
for i in glossário:
    sleep(1)
    print(f'=' * 65)
    print(f'{i} é {glossário[i]}')
    print(f'=' * 65)