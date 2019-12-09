#--- Exercicio 2  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um cliente
#--- Cliente: Nome, Sobrenome, ano de nascimento
#--- Exiba uma mensagem de boas vindas para o cliente
#--- Exiba um menu: Produtos alcoolicos e Produtos não alcoolicos, Sair
#--- Caso o cliente seja menor de idade o item 'produtos alcoolicos' não deve ser exibido
#--- Leia a opção digitada e crie uma tela para cada opção

nome = input('Informe seu nome\n')
sobrenome = input('Informe seu sobrenome\n')
nomecomp = nome +' '+ sobrenome
anodenasc = int(input('Informe seu ano de nascimento\n'))

idade = 2019 - anodenasc

if (idade >= 18):
    print('-'*30)
    print(f'Seja bem-vindo(a), {nomecomp}!\n\n1 - Produtos Alcoólicos.\n2 - Produtos Não-Alcoólicos.\n3 - Encerrar Programa.\n ')
    print('-'*30)
    op = int(input('\nEscolha uma opção:\n'))

    if(op == 1):
       print('-'*50)
       print('\tMarcas de Bebidas Alcoólicas AB InBev')
       print('1 - Antarctica.\n2 - Brahma.\n3 - Budweiser.\n4 - Corona.\n5 - Encerrar Programa.')
       print('-'*50) 
       opma = int(input('\nEscolha uma opção:\n'))
       
       if(opma == 1):
            print('Nome da Marca: Antarctica.\nTeor Alcoólico: 4,6% vol.\nMédia de Preço: R$3.50 unid.')
       elif(opma == 2):
            print('Nome da Marca: Brahma.\nTeor Alcoólico: 5% vol.\nMédia de Preço: R$3.10 unid.')   
       elif(opma == 3):
            print('Nome da Marca: Budweiser.\nTeor Alcoólico: 5% vol.\nMédia de Preço: R$2.10 unid.')
       elif(opma == 4):
            print('Nome da Marca: Corona.\nTeor Alcoólico: 4,5% vol.\nMédia de Preço: R$3.20 unid.')
       elif(opma == 5):
            SystemExit

    if(op == 2):
        print('-'*50)
        print('\tMarcas de Bebidas Não-Alcoólicas AB InBev')
        print('1 - Fusion.\n2 - Guaraná Antartica.\n3 - Pepsi.\n4 - Encerrar Programa.')
        print('-'*50)
        opmna = int(input('\nEscolha uma opção:\n'))

        if(opmna == 1):
            print('Nome da Marca: Fusion.\nTipo de Bebida: Energético.\nMédia de Preço: R$7.50 unid.')
        elif(opmna == 2):
            print('Nome da Marca: Guaraná Antartica.\nTipo de Bebida: Refrigerante.\nMédia de Preço: R$5.00 unid.')
        elif(opmna == 3):
            print('Nome da Marca: Pepsi.\nTipo de Bebida: Refrigerante.\nMédia de Preço: R$6.00 unid.')
        elif(opmna == 4):
            SystemExit

elif(idade < 18):
    print('-'*30)
    print(f'Seja bem-vindo(a), {nomecomp}!\n\n1 - Produtos Não-Alcoólicos.\n2 - Encerrar Programa.\n ')
    print('-'*30)
    op = int(input('\nEscolha uma opção:\n'))

    if(op == 1):
        print('-'*50)
        print('\tMarcas de Bebidas Não-Alcoólicas AB InBev')
        print('1 - Fusion.\n2 - Guaraná Antartica.\n3 - Pepsi.\n4 - Encerrar Programa.')
        print('-'*50)
        opmna = int(input('\nEscolha uma opção:\n'))

        if(opmna == 1):
            print('Nome da Marca: Fusion.\nTipo de Bebida: Energético.\nMédia de Preço: R$7.50 unid.')
        elif(opmna == 2):
            print('Nome da Marca: Guaraná Antartica.\nTipo de Bebida: Refrigerante.\nMédia de Preço: R$5.00 unid.')
        elif(opmna == 3):
            print('Nome da Marca: Pepsi.\nTipo de Bebida: Refrigerante.\nMédia de Preço: R$6.00 unid.')
        elif(opmna == 4):
            SystemExit

    elif(op == 2):
        SystemExit