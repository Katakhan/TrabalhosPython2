#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula
n1 = ''
n2 = ''
n3 = ''
med = '0'
def media(n1,n2,n3,med):
    n1 = float(input('Informe o 1 Número'))
    n2 = float(input('Informe o 2 Número'))
    n3 = float(input('Informe o 3 Número'))
    med = (n1+n2+n3)/3
    return print(f'A média entre {n1} , {n2}  e {n3} é: {med}')

media (n1,n2,n3,med) 