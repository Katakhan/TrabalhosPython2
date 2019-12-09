dicionario_bandas = {'nome' : 'dejavu'}
dicionario_bandas ['nome'] = 'Calipso'
dicionario_bandas ['nome'] = 'dejavu'

print(dicionario_bandas)

dicionario = {'nome':'antonio', 'Sobrenome': 'Gastaldi'}
dicionario['Sobrenome'] = 'Rafael'
dicionario['cpf'] = '053.654.354-47'

dicionario_pessoa = {'Nome' : '' ,'Sobrenome' : '', 'Cpf':'','RG':''}

lista_pessoa = []
for i in range(1,11):
    dicionario_pessoa ['Nome'] = input('Digite o nome')
    dicionario_pessoa ['Sobrenome'] = input('Digite o sobrenome')
    dicionario_pessoa ['Cpf'] = input('Digite o CPF')
    dicionario_pessoa ['RG'] = input('Digite o RG')
    lista_pessoa.append ( dicionario_pessoa )
print(lista_pessoa)