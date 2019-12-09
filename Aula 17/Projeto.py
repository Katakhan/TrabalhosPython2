# 1 - O programa deve ter um menu interativo com cabeçalho, local para:
# cadastro de clientes.
# ver clientes cadastrados, cadastro de produtos, ver produtos
# cadastrados, venda de produtos,
# relatorio de vendas e a opção sair
# este menu deve se repetir até que a opção sair for chamado

menu = '''
###############################################################################
#                        1 Festival de cervaja em Ituroró                     #
###############################################################################

1 -  Cadastro de Cliente
2 - Ver clientes Cadastrados
3 - Cadastro de produtos
4 - Ver produtos Cadastrados
5 - Vendas
6 - Relatório de Vendas
7 - Sair

Digite a opção desejada '''

# opcao = input(menu)
while True:
    opcao = input(menu)
    if opcao == '1':
        print ('Cadastro De Cliente')
    if opcao == '2':
        print('Ver clientes Cadastrados')
    if opcao =='3':
        print('Cadastro de produtos')
    if opcao == '4':
        print('Ver produtos Cadastrados')
    if opcao == '5':
        print('Vendas')
    if opcao == '6':
        print('Relatório de vendas')
    if opcao == '7':
        print('Sair')
        break
    else :
        print('opção invalida')
        opcao = input(menu)