#2- Mercado tech...
#Solicitar Nome do funcionario
#solicitar idade
#informar se o funcionario pode adquirir produtos alcoolicos


#3-
#cadastrar produtos mercado tech
#solicitar nome do produto
#Solicitar a categoria do produto(alcoolicos e não alcoolicos)
#exibir o produto cadastrado


nomef = input('informe o nome do funcionário: ')
idade = int(input('informe a idade :' ))

if idade >=18:
    print(f'pode dale na cachaça,{nomef}')
else:
    print(f'Vai chapar de energético só se for{nomef}')
