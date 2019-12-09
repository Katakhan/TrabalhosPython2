#aula 6 P2 - 13-11-2019
#Estruturas de repetição - FOR

#For simples usando range com incremento padrão de 1
#for i in range(0,10):
  #  print(f'{i}-Padawans HbPy')

#For usando range com incremento de 2
#for i in range(0,100,2):
 #   print(f'{i}- Pares')



lista = ['Mateus','Matheus','Marcela','Nicole','Tonho','Pablo']
# #for i in range (0,6):
#     #print(lista[i])

for i in range (0,7):
    lista.append('Natan')
    print(lista[i])

n = 10
for i in range (0,10):
    print(f'{i} x {n} = {i*n}')