#3- crie um programa para calculo de investimento
# solicitar valor a ser investido no tesouro selic
# calcular o valor do vencimento do titulo
# utilizar metodos  



pt = float(input('Informe quantas cotas deseja comprar? 1 cota = 10410.00'))
valor_investido = pt *10410
print(valor_investido)
valor_final = (valor_investido *0.05)*64
if pt >= 0.01 :
    print('O investimento renderá 5% ao ano')
    print(f'O valor final será: {valor_final+pt+valor_investido}')
