marca = input('Informe a marca da cerveja')
teor = float(input('informe o teor alcoolico da cerveja'))
tipo = input('Informe o tipo da cervaja(Alcoolico(1) e não alcoolico (0))')

cerva_dicionario = {'marca':marca, 'Teor':teor, 'Tipo':tipo}


def salvar_cerva(cerva_dicionario):
    arquivo = open ('Banco de cerva.txt','a')
    arquivo.write(f"{cerva_dicionario['marca']};{cerva_dicionario['teor']};{cerva_dicionario['tipo']}\n")
    arquivo.close()
def ler():
    lista = []  
    arquivo = open ('Banco de cerva.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerva = {'marca':lista_linha[0] , 'teor':lista_linha[1], 'tipo':lista_linha[2]}
        lista.append(cerva)
        arquivo.close
    return lista

def salvar(cerva):
     arquivo = open ('Banco de cerva.txt', 'r')
     for linha in arquivo:
      print('linha')
     arquivo.closed

nome = input('Informe seu nome: \n')
sobrenome = input('Informe seu Sobrenome: \n')
idade = int(input('Informe sua idade: \n'))

cerva = {'nome':nome , 'sobrenome':sobrenome, 'idade':idade}

salvar_cerva(cerva)
lista = ler()
for p in lista:
    print(f"{p['marca']} - {p['teor']} - {p['tipo']}")