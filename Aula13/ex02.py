#Use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e pergunte quais seus número favoritos. Use seus nomes para serem as chaves de cada número favorito. Ao final, exiba o nome de cada pessoas e seu número favorito.
resposta = {'Junior': 15, 'Sofia': 9, 'Thiago': 23, 'Lara': 8, 'Lucas': 3}
print(f'=' * 55)
print(f'Os números favoritos dos amigos são: {resposta.items()}')
print(f'=' * 55)
for k, v in resposta.items():# k signica o keys e v = values 
    print(f'Os números favoritos de {k} = {v}')
print(f'=' * 55)
