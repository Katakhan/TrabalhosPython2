#2- crie um programa que calcule a rentabilidade anual de um investimento baseando-se em sua rentabilidade mensal(juros compostos)
# e a rentablidade deve ser apresentada em % e R$ utilizar metodos



from Aula11 import *
investimento = float(input('Digite o valor do investimento: R$'))
taxa = float(input('Informe a taxa que deseja investir: '))
taxa = taxa/100
mes = int(input('Informe a quantidade de meses que deseja investir: '))

vinvest = invest(investimento,mes,taxa)
print(f'O valor do seu investimento de {mes} meses vai ser de R${vinvest}/Lucro de {(vinvest-investimento)}%')