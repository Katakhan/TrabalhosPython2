# crie um programa que leia 4 notas
#imprima a maior
# imprima a menor
#imprima a media
#imprima se o aluno foi aprovado ou reprovado (Média 7 )
n1 = float(input('Insira sua 1 Nota'))
n2 = float(input('Insira sua 2 Nota'))
n3 = float(input('Insira sua 3 Nota'))
n4 = float(input('Insira sua 4 Nota'))
 

if n1 > n2 and n1>n3 and n1>n4:
    print(f'A maior nota é: {n1}')  

elif n2 > n1 and n2>n3 and n2>n4:
    print(f'A maior nota é :{n2}')

elif n3 > n1 and n3>n2 and n3>n4:
    print(f'A maior nota é :{n3}')

else:
    print(f'a maior nota é: {n4}')

if n1>n2:
    print(f'A menor nota é: {n2}')

elif n2 > n3:
    print(f'A menor nota é :{n3}')

elif n3 > n4 :
    print(f'A menor nota é : {n4}')

else:
    print(f'a menor nota é: {n1}')


media = (n1+n2+n3+n4)/4
print(f'A média é: {media}')

if media >= 7:
    print('aluno aprovado')
else:
    print('aluno reprovado')
    