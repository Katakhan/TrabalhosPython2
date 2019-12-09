# Exercicio 2  - dicionarios
# Escreva um programa que leia dados de 11 jogadores
# jogador: Nome,Posicao, Numero, PernaBoa
# crie um dicionario para armazenar os dados
# imprima todosos jogadores e seus dados

lista_time = []
for i in range(0,3):
    jogador = {'Nome': '','Posicao':'', 'Numero':'','Pernaboa':''}
    jogador['Nome'] = input('informe o nome do jogador')
    jogador['Posicao'] = input('informe a posição do jogador')
    jogador['Numero'] = input('informe o numero do jogador')
    jogador['Pernaboa'] = input('informe a Perna Boa do jogador')
    lista_time.append(jogador)
for j in lista_time:
    print(f'dados do jogador{j}')
