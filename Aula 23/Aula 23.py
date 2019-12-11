# numero_inicial = int(input('Qual o Numero que vocÊ deseja começar a somar?'))
# numero_final = int(input('Até qual numero devemos somar?'))
# total = 0
# for numero in range(numero_inicial,numero_final+1):
#     total += numero

# print(total)

# total = 0
# for numero in [50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65] + list(range(66,101 )):
#     total += numero

# print(f'Total gohorse: {total}')

# texto = 'Tenho saudades do prof abio, Python é legal, Gabriel Pensador'
# print(texto.split(','))

# def nosso_split(txt, sep):
#    result = []
#    count = 0
#    for char in txt:
#         if char == sep:
#             result.append(txt[0:count])
#         count += 1
#     return result

# print(nosso_split(texto, ','))


dias_de_cada_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

qual_mes = int(input('Digite o número do mês (1..12): '))

print('O mês', qual_mes, 'tem', dias_de_cada_mes[qual_mes], 'dias')

# print('Dias que faltam para acabar o ano, a partir de mês informado: ')
# print(sum(list(dias_de_cada_mes.values())[qual_mes-1:]))

total = 0
for mes in range(qual_mes, 12+1):
    total += dias_de_cada_mes[mes]
print('Modo Estruturado')
print('Total de dias até o final de ano', total)

for chave in dias_de_cada_mes:
    print(f'Tenho uma chave nessa linha: {chave}')
    print(f'Se tenho a chave, tenho o valor: {dias_de_cada_mes[chave]}')

for chave, valor in dias_de_cada_mes.items():
    print(f'Para a chave {chave} o valor {valor}')
