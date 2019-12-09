#aula 7 14-11-2019
#Dicionarios

lista = []
dicionario = { 'Nome': 'Antonio' , 'Sobrenome' : 'Gastaldi' }
print(dicionario)
print(dicionario['Sobrenome'])

nome = 'Antônio'
lista_notas = [10,20,50,70]

media = sum(lista_notas)/ len(lista_notas)
situacao = 'Reprovado'

if media >= 7 :  
    situacao = 'Aprovado'
dicionario_alunos = {'nome' :nome, 'lista_Notas': lista_notas, 'Media' : media, 'Situacao': situacao }
print(f"{dicionario_alunos['nome']} - {dicionario_alunos['Situacao']}")