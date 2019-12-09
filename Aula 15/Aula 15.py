## Aula 15 -28/11/2002
## Manipulação de arquivos

# arquivo = open ('aula15.txt','x')
# arquivo.write('Voltoline Turismo\n')
# arquivo.close()

# arquivo = open ('Aula15.txt', 'r')
# for linha in arquivo:
#     print('linha')
# arquivo.closed


def salvar_pessoa(pessoa_dicionario):
    arquivo = open ('Aula15.txt','a')
    arquivo.write(f"{pessoa_dicionario['nome']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']}\n")
    arquivo.close()
def ler():
    lista = []  
    arquivo = open ('Aula15.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome':lista_linha[0] , 'sobrenome':lista_linha[1], 'idade':lista_linha[2]}
        lista.append(pessoa)
        arquivo.close
    return lista

def salvar(pessoa):
     arquivo = open ('Aula15.txt', 'r')
     for linha in arquivo:
      print('linha')
     arquivo.closed

nome = input('Informe seu nome: \n')
sobrenome = input('Informe seu Sobrenome: \n')
idade = int(input('Informe sua idade: \n'))

pessoa = {'nome':nome , 'sobrenome':sobrenome, 'idade':idade}

salvar_pessoa(pessoa)
lista = ler()
for p in lista:
    print(f"{p['nome']} - {p['sobrenome']} - {p['idade']}")