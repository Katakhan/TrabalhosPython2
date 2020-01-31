from flask_restful import Resource
from Dao.pessoa_dao import PessoaDao


class PessoaDao(Resource):

    def __init__(self):
        self.dao = PessoaDao()

    def list_all(self):
        return 'Listando todos os dados da tabela'

    def get_by_id(self, id):
        return f'Listando o dado de ID: {}'.format(id)

    def inset(self, pessoa):
        return 'Cadastrando uma pessoa'

    def update(self, pessoa):
        return 'Alterando uma pessoa'

    def remove(self, id):
        return f'Removendo uma pessoa pelo id:{}'.format(id)

    from flask_restful import Resource