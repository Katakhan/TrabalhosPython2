#--- Exercicio 3  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um funcionário
#--- Funcionário: Nome Completo, CPF, Número do registro, Cargo e Salário
#--- Exiba os dados de salário liquido, descontando os tributos
#--- Deve ser calculado o valor do INSS -
#--- INSS -  de    0,00 ate 1751,81 - percetual =  8,0%
#---         de 1751,82 ate 2919,72 - percetual =  9,5%
#---         de 2919,72 ate 5839,45 - percetual = 11,0%
#--- Deve ser calculado o valor do IRRF - 
#--- IRRF -  de    0,00 ate 1903,98 - percetual =  0,0%
#---         de 1903,98 ate 2826,65 - percetual =  7,5%
#---         de 2826,66 ate 3751,05 - percetual = 15,0%
#---         de 3751,06 ate 4664,68 - percetual = 22,5%
#---         de 4664,69 ate ------- - percetual = 27,5%
#--- Base - http://www.calculador.com.br/calculo/salario-liquido

nome = input('Informe o nome completo do funcionário\n')
cpf = input('Informe o CPF do funcionário\n')
rg = input('Informe o número de registros do funcionário\n')
cargo = input('Informe o cargo do funcionário\n')
sal_ini = float(input('Informe o salário do funcionário\n'))

if(sal_ini >= 0) and (sal_ini <= 1751.81):
    tribinss = sal_ini * 0.08
elif(sal_ini >= 1751.82) and (sal_ini <= 2919.72):
    tribinss = sal_ini * 0.095
elif(sal_ini > 2919.72) and (sal_ini <= 5839.45):
    tribinss = sal_ini * 0.11
    
sal_define = sal_ini - tribinss

if(sal_define >= 0) and (sal_define < 1903.98):
    ali = 0
    ded = 0
elif(sal_define >= 1903.98) and (sal_define <= 2826.65):
    ali = 0.075
    ded = 142.80
elif(sal_define >= 2826.66) and (sal_define <= 3751.05):
    ali = 0.15
    ded = 354.80
elif(sal_define >= 3751.06) and (sal_define <= 4664.68):
    ali = 0.225
    ded = 636.13
elif(sal_define >= 4664.69):
    ali = 0.275
    ded = 869.36

tribsirf = (((sal_ini - tribinss)*ali)-ded)
tribstot = tribinss + tribsirf
salliq = sal_ini - tribstot

print(f'Nome Completo: {nome}.\nCPF: {cpf}.\nRG: {rg}.\nCargo: {cargo}.\nSalário Bruto: {sal_ini}.\nSalário Líquido: {salliq}.')
print(f'\nTributos do INSS: {round(tribinss , 2)} | Tributos do Imposto de Renda: {round(tribsirf , 2)} | Total de Tributos: {round(tribstot , 2)}.')