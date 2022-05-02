# 7) PROGRAMA COTAÇÃO – O usuário digita quanto está valendo o dólar e quanto em reais ele possui. O programa exibe quantos dólares valem os reais que o usuário informou. 

dolar = float(input('Digite o Valor do dolar: '))
cot_real = float(input('Quantos reais você quer saber em dolar? '))
result = cot_real / dolar
print(f'O valor em real que o você digitou é: {result} ')