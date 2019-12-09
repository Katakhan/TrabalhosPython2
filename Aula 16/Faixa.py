
def faixa(musica,album,artista):
    playlist = {'musica':musica, 'artista':artista, 'album':album}
    return playlist


def salvar (faixa):
    arquivo = open ('Faixa.txt', 'a')
    arquivo.write(f"{faixa['musica']} ; {faixa['artista']} ; {faixa['album']}\n")
    arquivo.close()

def ler():
    arquivo = open ('Faixa.txt', 'r')
    lista =[]
    for linha in arquivo:
        linha = linha.strip()
        dadosfaixa = linha.split(';')
        Faixa = faixa(dadosfaixa[0],dadosfaixa[1],dadosfaixa[2])
        lista.append(Faixa) 
    arquivo.close()
    return lista