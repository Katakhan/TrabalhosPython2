import sys
sys.path.append(r'C:\Users\900132\Desktop\GitHub\TrabalhosPython2\Aula 37')
from Dao.sqbds_dao import SgbdsDao
from Model.sgbds import Sgbds

class SgbdsController:
    dao = SgbdsDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, sgbds:Sgbds):
        return self.dao.salvar(sgbds)

    def alterar(self, sgbds:Sgbds):
        self.dao.alterar(sgbds)

    def deletar(self, id):
        self.dao.deletar(id)
