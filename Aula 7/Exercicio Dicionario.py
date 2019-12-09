# #Exercicio Dicionario 1
# escreva um programa que leia dados de cerveja
# cerveja: Marca, tipo, ibu ,abv, volume, ebc 
#crie um dicionario para armazenar os dados 
#imprima os dados do dicionario (não dicionario completo)

marca = input('informe a marca da cerveja')
tipo = input('Qual é o tipo da cerveja')
ibu = input(int('informe o ibu'))
abv = input(float('informe o abv'))
ebc = input(float('informe o ebc'))
volume = input('informe o volume')

cerveja = {'marca': marca, 'tipo' : tipo, 'ibu' : ibu, 'abv' : abv, 'ebc' : ebc, 'volume' : volume}

print(f"'Marca{cerveja['marca']} - {cerveja['tipo']} - {cerveja['ibu']} - {cerveja['abv']} - {cerveja['ebc']} - {cerveja['volume']}")
