## 29/11/2019 -  Aula 16
##


## Cadastro de playlist
## Lendo Musica, Artista E album

from Faixa import faixa,salvar,ler


musica = input('Informe o nome da Musica \n')
artista = input('Informe o nome do Artista \n')
album = input('Informe o nome do Album \n')



faixa = faixa(musica,album,artista)
salvar(faixa) 
lista_ler = ler()

for faixa in lista_ler:
    print(f"{faixa['musica']} | {faixa['artista']} | {faixa['album']}")