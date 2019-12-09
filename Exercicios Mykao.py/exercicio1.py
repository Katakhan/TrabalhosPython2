#--- Exercicio 1  - Variávies e impressão com interpolacão de string
#--- Crie 5 variávies para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Os dados devem ser impressos utilizando a funcao format()
#--- Deve ser usado apenas uma vez a função print(), porem os dados devem ser apresentados um em cada linha
#--- O salario deve ser de tipo flutuante e na impressão deve apesentar apenas duas casas após a vírgula

nome = input('Insira seu nome')
sobrenome = input('Insira seu sobrenome')
cpf = input('Insira seu Cpf')
rg = input('Insira seu RG')
salario = float(input('Insira seu Salario'))


print (f'Nome: {nome},\n Sobrenome: {sobrenome},\n CPF: {cpf} ,\n RG: {rg} ,\n Salario: {salario} ')