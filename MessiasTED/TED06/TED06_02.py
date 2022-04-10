#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano = 2022
nascimento = int(input('Digita o ano que você nasceu: '))
votar = 2022 - nascimento
if votar >= 16:
    (print('Voce poderá votar nessas eleições'))
else: 
    (print('Você não poderá votar esse ano'))