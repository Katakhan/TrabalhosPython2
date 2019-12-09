#--- Exercicio 4  - Impressão de dados com a função Input
#--- Crie a tela inicial para um sistema de compra de bebidas 
#--- A tela deve conter cabeçalho, menu, tela de boas vindas e rodapé


print ('=='*50)
print ('                                             ', 'Bem vindo' '                                             ')
produto1 = 'Corona'
produto = 'Coca Cola'
categoria = input ('\n \t  Deseja comprar itens alcoolicos ou não alcoolicos?  \n \t  Para alcoolicos Digite 1 e para Não alcoolicos 2: ')

if categoria == '1' :
    print(f'          O produto escolhido é alcoolico \n          nome do produto: {produto1}')
    print ('=='*50)
else:
    print(f'          O produto escolhido não é alcoolico \n          nome do produto: {produto}')
    print ('=='*50)