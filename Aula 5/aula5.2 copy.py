#3-
#cadastrar produtos mercado tech
#solicitar nome do produto
#Solicitar a categoria do produto(alcoolicos e não alcoolicos)
#exibir o produto cadastrado

produto = input('informe o nome do produto')
categoria = input('informe a categoria, 1- alcoolico e 2-não alcoolico')

if categoria == '1' :
    print(f'O produto escolhido é alcoolico \n nome do produto: {produto}')
else:
    print(f'O produto escolhido não é alcoolico \n nome do produto: {produto}')