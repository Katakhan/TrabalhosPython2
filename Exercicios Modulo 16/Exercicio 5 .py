#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)
determ = ''
n1 = ''
raiz = ''
def calcraiz (determ, n1 ,raiz):
    determ = float(input('Informe o determinante: 2,3,4 \n'))
    n1 = float(input('Informe o numero que deseja obter a raiz\n'))
    raiz = n1 **  (1/determ)
    return print(f'O resultado da raiz {determ} de {n1} é {raiz}')

calcraiz(determ ,n1, raiz)
