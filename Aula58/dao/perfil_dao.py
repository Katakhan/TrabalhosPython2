from Aula58.model.perfil_model import Perfil

class PerfilDao:
    def list_all(self):
        arquivo = open(r'C:\Users\900132\Desktop\GitHub\TrabalhosPython2\Aula58\perfil.txt', 'r')
        lista_perfil = []
        for i in arquivo:
            i = i.strip().split(';')

            lista_perfil.append(i)

        return lista_perfil

