n1 = int(input('Escreva um numero: '))
n2 = int(input('Escreva outro número: '))



print('\n'*2, '='*50)

resultado1 = n1 + n2
resultado2 = n1 - n2
resultado3 = n1 / n2
resultado4 = n1 * n2


print(f'Soma: {n1} + {n2} = {resultado1}')
print(f'Subtração: {n1} - {n2} = {resultado2}')
print(f'Divisão: {n1} / {n2} = {resultado3}')
print(f'Multiplicação: {n1} * {n2} = {resultado4}')

print('\n'*2, '='*50)


if n1 > n2 :
    print(f'O Maior Número é: {n1}')

elif n1 == n2:
    print('Os numeros são iguais')
    print('Não há numero maior')

else:

    print (f'O maior Número é: {n2}')

