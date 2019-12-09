#--- Exercício 4 - Funções - 2
#--- Crie uma função que realize o cálculo de contribuição do funcionário para a previdência da empresa
#--- O cálculo deve ser feito de acordo com a faixa salarial:
#---    De R$ 0000.00 Até R$ 1000.00 -> 1.0%
#---    De R$ 1000.01 Até R$ 3000.00 -> 1.5%
#---    De R$ 3000.01 Até R$ 6000.00 -> 2.0%
#---    Acima de R$ 6000.01 -> 2.5%
#--- A função deve receber o valor do salário
#--- A função deve fazer o cálculo de acordo com as regras de faixa salárial e atribuir o resultado em uma variável
#--- O resultado deve ser impresso pela função juntamente com uma frase e utilizando f-string
#--- Deve ser realizada a leitura do salário fora da função e armazenada em uma variável
#--- Chamar a função e passar a variável do salário criada durante a leitura do console

sal = float(input('Informe o Seu salario'))

def calc (sal):
    if sal <= 1000:
        contribu = sal * 0.01
    elif sal >1000 <=3000:
        contribu = sal * 0.015
    elif sal >3000 <=6000:
        contribu = sal * 0.02
    elif sal >6000:
        contribu = sal *0.025
    else :
        print ('Salario invalido')
    return contribu
r = calc(sal)
print(f'A contribuição será de {r:0.2f} reais para a previdencia da empresa')