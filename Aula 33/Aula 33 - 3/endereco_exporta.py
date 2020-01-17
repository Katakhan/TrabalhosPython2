def exportar_txt(lista_endereco):
    with open('Aula 33/Aula 33 - 3/endereco.txt','a') as arquivo:
        for e in lista_endereco:
            arquivo.write(f"{e['Id']};{e['Logradouro']};{e['Numero']};{e['Complemento']};{e['Bairro']};{e['Cidade']};{e['Cep']}\n")