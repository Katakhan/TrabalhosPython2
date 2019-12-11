# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

class Cliente:
    '''
    Esta classe é uma demonstração para aula
    '''
    def __init__ (self,dadobruto):
        ''' 
        O __init__ é o motor que irá iniciar as variáveis da clase
        O self é o que irá conecta toda a classe
        '''
        # Atributos ##########
        self.dadobruto = dadobruto.split(';')
        self.nome = None
        self.idade = None
        self.telefone = None
        self.sexo = None
        self.email = None
        self.codigo = None
        self.atualizar (self.dadobruto[0],self.dadobruto[1],self.dadobruto[2],self.dadobruto[3],self.dadobruto[4],self.dadobruto[5])

    def imprimir(self):
        print(f'Nome é {self.nome}')
        print(f'Codigo do cliente {self.codigo}')
        print(f'Idade do Cliente {self.idade}')
        print(f'Email do Cliente: {self.email}')
        print(f'Telefone do Cliente: {self.telefone}')
        print(f'Sexo do Cliente: {self.sexo}')

    def salvar(self):
        arquivo = open ('Aula 23/Aula23.txt','a')
        arquivo.write(f'{self.nome},{self.email},{self.codigo},{self.idade},{self.sexo} {self.telefone}')
        arquivo.close()

    def atualizar(self,codigo,nome,idade,sexo,email,telefone):
        self.codigo = int(codigo)
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.dados_cliente= f'{codigo};{nome};{idade};{sexo};{email};{telefone} \n'

# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

arquivo = open('Aula 23/Aula23.txt','a')
dados_cliente = Cliente('1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117')
dados_cliente.imprimir()
dados_cliente.atualizar(1,'Tonhao',15,'m','xesquedeledale@gmail.com','14234234324')
dados_cliente.salvar()
