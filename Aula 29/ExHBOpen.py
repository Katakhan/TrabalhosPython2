terminal = ['piloto','official1','official2','comissaria1','comissaria2','chefe','policial','ladrao']

def defterminal (terminal):
    lista = []
    dados = ','.join(terminal) # Convertendo uma lista em String e atribuindo ela a variável dados
    arquivo = open('Aula 29/terminal.txt', 'w') # Criando arquivo
    arquivo.write(dados)  # Inserindo conteúdo no arquivo
    lista.append(dados) # Inserindo na lista os dados do arquivo
    arquivo.close() # Fehando arquivo
    return lista

def defaviao (embarcados x):
    dados = ','.join(embarcados)       
    arquivo = open('Aula 29/aviao.txt', 'w') # Criando arquivo
    arquivo.write(dados)  # Inserindo conteúdo no arquivo
    arquivo.close() # Fehando arquivo