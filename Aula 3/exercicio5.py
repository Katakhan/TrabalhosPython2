#--- Exercicio 5  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia o salário de uma pessoa
#--- Use o método 50-20-10-20 - https://www.jaseimevirar.com/blog/como-voce-organiza-seu-orcamento-mensal/
#--- Informe os percentuais e valores que a pessoa deve utilizar em cada categoria
#--- Deve ser utilizado a função format e os caracteres de tabulação e quebra de linha para cada categoria

nome = input('Informe o seu nome\n')
sal = float(input('Informe seu salário\n'))

dfix = sal * 0.5
inveslong = sal * 0.2
invescurt = sal * 0.1
despsvar = sal * 0.2

print(f'Nome do Usuário: {nome}.\nSalário Total: {sal}.\nPorcentagem para Despesas Fixas: {dfix}.\nPorcentagem para Investimentos de Longo Prazo: {inveslong}.\nPorcentagem para Investimentos de Curto Prazo: {invescurt}.\nPorcentagem para Gastos Livres e Despesas Variáveis: {despsvar}')