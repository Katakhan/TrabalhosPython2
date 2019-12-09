#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console
n1 = ''
n2 = ''
r = ''

n1 = float(input('Informe o 1 número'))
n2 = float(input('Informe o 2 Número'))

def calc(n1,n2):
    r = n1*n2
    return r


pó = calc(n1,n2)
print(f'O resultado da multiplicação entre {n1} * {n2} é : {pó:0.2f}')

##44