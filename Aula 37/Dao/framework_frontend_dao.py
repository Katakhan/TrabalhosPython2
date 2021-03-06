import sys
sys.path.append(r'C:\Users\900132\Desktop\GitHub\TrabalhosPython2\Aula 37')
import MySQLdb
from Model.framework_frontend import FrameworkFrontend


class FrontDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans11', user='padawans11', passwd='at2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM FrameworkFrontend"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM FrameworkFrontend WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, FrameworkFrontend:FrameworkFrontend):
        comando = f""" INSERT INTO FrameworkFrontend
        (
            nome
        )
        VALUES
        (
            '{FrameworkFrontend.nome}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, FrameworkFrontend:FrameworkFrontend):
        comando = f""" UPDATE FrameworkFrontend
        SET
            nome = '{FrameworkFrontend.nome}'
            
        WHERE ID = {FrameworkFrontend.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM FrameworkFrontend WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()