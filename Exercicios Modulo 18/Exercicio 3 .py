#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados
sist = ''
carac = ''
def cabeçalho (sist,carac):
    
    sist = input('informe o nome do sistem')
    carac = input('Informe o caractere para o cabeçalho')
    return print(f'{carac*50} Nome do sistema é: {sist} {carac*50}')

cabeçalho(sist,carac)
