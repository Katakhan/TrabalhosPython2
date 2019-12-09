
from operacoes import cadicao,cdivisao,cmultiplicacao,cpotenciacao,csubtracao,craiz,cresto

n1 = float(input('informe o primeiro numero'))
n2 = float(input('informe o segundo numero'))

adicao = cadicao(n1,n2)
subtracao = csubtracao(n1,n2)
multiplicacao = cmultiplicacao(n1,n2)
potenciacao = cpotenciacao(n1,n2)
divisao = cdivisao(n1,n2)
resto = cresto(n1,n2)
print(f'Resultado da Adição entre {n1} e {n2} é : {adicao}')
print(f'Resultado da subtração entre {n1} e {n2} é : {subtracao}')
print(f'Resultado da multiplicacao entre {n1} e {n2} é : {multiplicacao}')
print(f'Resultado da potenciação entre {n1} e {n2} é : {potenciacao}')
print(f'Resultado da divisao entre {n1} e {n2} é :{divisao}')
print(f'o resto é: {resto}')
