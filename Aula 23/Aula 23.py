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

d_mes = {
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
q_mes = int(input('Informe o numero do mes'))
print('O med',q_mes,'tem', d_mes[q_mes],'dias')
