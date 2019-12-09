#  1- Faça um menu interativo que tenha: Cadastro da banda, Cadastro
#  do album, cadastro da musica, Sair.
#  O menu deve ser executado até que se escolha a opção Sair
#  cada opção deve ser mostrada
#  quando selecionado a opção sair deverá aparecer na tela as 
#  informações das bandas cadastradas
#  albuns e musicas

menu = '''
###############################################################################
#                        1 Festival de cervaja em Ituroró                     #
###############################################################################

1 -  Cadastro da Banda
2 - Cadastro do Album
3 - Cadastro Da Musica
4 - Sair

Digite a opção desejada '''

banda = []
album = []
musica = []

while True :
    opcao = input(menu)

    if opcao == '1':
        print('Opção selecionada Cadastro de banda')
        banda.append(input('Informe O nome da banda'))


    elif opcao == '2':
        print('Opção selecionada Cadastro de album')
        album.append(input('Informe O nome da banda'))


    elif opcao =='3':
        print('Opção selecionada Cadastro de Musica')
        musica.append(input('Informe O nome da Musica'))


    elif opcao =='4':
        print('Opção selecionada Sair')
        print(f'O nome das bandas informadas é{banda}\n Os Albuns informados são: {album} \n As musicas Cadastradas são: {musica}')
        break

    else : 
        print('opção invalida')