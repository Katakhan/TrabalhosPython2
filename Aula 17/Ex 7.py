    def cadastro_cliente(numero_funcao):
    dados = ['codigo_cli', 'cpf' , 'nome',
            'data_nasc', 'estado', 'cidade'
            'cep', 'bairro', 'rua', 'numero_casa', 'complemento']
    lista = []

numero = int(input('Informe o número de cadastros'))

    for k in range(numero):
        dicionario = {}
            
        for i in dados:
            dicionario[i] = input(f' {i}: ')
        lista.append(dicionario)

        print(dicionario)
        print(lista)
        return lista

lista = cadastro_cliente(numero)

#criar uma função para salvar em arquivo:

arquivo = open ('clientes.txt','a')
for cliente in arquivo:
    salvar = f'{cliente['codigo_cli']}'

arquivo.write()

arquivo.close()