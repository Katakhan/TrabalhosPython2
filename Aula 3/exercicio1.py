#--- Exercicio 1  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia dois números inteiros
#--- Realize as 4 operações matemáticas básicas com os números lidos
#--- Imprima os resultados das operações 
#--- Informe qual número é maior ou se os dois são iguais

x = int(input('Informe o primeiro número\n'))
y = int(input('Informe o segundo número\n'))

soma = x + y
sub = x - y
multi = x * y
div = x / y

print(f'Adição: {soma}\nSubtração: {sub}\nMultiplicação: {multi}\nDivisão: {div}')

if(x > y):
    print(f'O primeiro número ({x}) é maior que o segundo número ({y})')
elif(y > x):
    print(f'O segundo número ({y}) é maior que o primeiro número ({x})')
elif(x == y):
    print('Os dois números são iguais')