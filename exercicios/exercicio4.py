#--- Exercicio 4  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que realize a autenticação de usuário
#--- Crie duas variáveis para conter o usuário e senha padrão do sistema
#--- Leia o usuário e senha informados pelo usuário via função input()
#--- Valide se usuário e senha estão corretos
#--- Caso o usuário e senha estejam corretos informe com mensagem de boas vindas
#--- Caso o usuário e senha estejam incorretos informe com mensagem de falha de login

login = 'tonhaopoucas'
senha = 'balas'

newLogin = input('Informe o login\n')
newSenha = input('Informe a senha\n')

if((newLogin == login) and (newSenha==senha)):
    print(f'Seja bem-vindo, {login}!')
else:
    print('Falha no login!')