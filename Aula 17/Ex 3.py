# Faça um programa que leia um numero inteiro de 1 a 10 no teclado e mostre se você acertou ou
# o numero digitado é maior ou menos
# quando voce acertar o programa deverá ser finalizado

from random import randint
aleatorio = randint(1,10)
print(aleatorio)


nr = 0
while True:
    nr = int(input('Informe um numero de 1 a 10: '))
    
    if nr == aleatorio:
        print('Parabens você acertou o numero')
        break
    elif nr > aleatorio:
        print('O numero informado é maior que o Numero Aleatorio')
    else : 
        print('O numero informado é menor que o Numero Aleatorio')
