# 21-11-2019 - Prova
#-1 Crie um programa que calcule o ISS de um serviço de desenvolvimento de software
#2- crie um programa que calcule a rentabilidade anual de um investimento baseando-se em sua rentabilidade mensal(juros compostos)
# e a rentablidade deve ser apresentada em % e R$ utilizar metodos
#3- crie um programa para calculo de investimento
# solicitar valor a ser investido no tesouro selic
# calcular o valor do vencimento do titulo
# utilizar metodos  
#4-10410.00 
#5- 

from Aula11 import * 


tpagar = float(input('informe o custo do projeto'))

iss = iss1( tpagar)
print (f'O total a pagar é: {iss}')