#--- Exercicio 2  - Variávies e impressão com interpolacão de string
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format() para concatenar os números da opções, que devem ser números inteiros
#--- Alem das opções o menu deve conter um cabeçalho e um rodapé
#--- O cabeçalho e o rodapé devem ser impressos utilizando a multiplicação de caracters
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação




print ('=='*50)
print ('-'*45,'Bem vindo','-'*45,'\n'*3)

opcao = input('informe o numero da opcao desejada \n \t 1- cadastrar funcionario \n \t 2 - sair \n \t Opção desejada : ')
if opcao == '1':
    funcionario = input('informe o nome do funcionario')
    print(f'Nome do funcionario: {funcionario}')
else: 
    '\n'*3
    exit
print('\n'*3)
print ('=='*50)
print ('-'*45,'Finalizando','-'*45,)