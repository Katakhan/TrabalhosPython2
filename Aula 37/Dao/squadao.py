import MySQLdb
import sys
sys.path.append(r'C:\Users\900132\Desktop\GitHub\TrabalhosPython2\Aula 37')

from Model import *

class SquaDao:
    conexao = MySQLdb.connect(host='localhost', database='squads', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM squads_2 "
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM squads_2 WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO 01_MDG_PESSOA
        (
            ID,
            DESCRICAO,
            NUMEROPESSOAS,
            LINGUAGEMBACKEND,
            FRAMEWORKFRONTEND,
            NOMESQUAD
        )
        VALUES
        (
            {squad.id},
            '{squad.Descricao},
            {squad.numeropessoas},
            '{squad.linguagembackend}',
            '{squad.frameworkfrontend}',
            '{nomesquad}',

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    # def alterar(self, pessoa:Pessoa):
    #     comando = f""" UPDATE 01_MDG_PESSOA
    #     SET
    #         NOME = '{pessoa.nome}',
    #         SOBRENOME ='{pessoa.sobrenome}',
    #         IDADE = {pessoa.idade},
    #         ENDERECO_ID = {pessoa.endereco.id}
    #     WHERE ID = {pessoa.id}
    #     """
    #     self.cursor.execute(comando)
    #     self.conexao.commit()

    # def deletar(self, id):
    #     comando = f"DELETE FROM 01_MDG_PESSOA WHERE ID = {id}"
    #     self.cursor.execute(comando)
    #     self.conexao.commit()

squadao = SquaDao()
squad = Squad()
squad.salvar('')
print(b)
