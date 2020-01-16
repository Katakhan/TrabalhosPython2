import sys
sys.path.append('C:\Users\900132\Desktop\GitHub\TrabalhosPython2\Aula 33\Aula 33 - 4')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)