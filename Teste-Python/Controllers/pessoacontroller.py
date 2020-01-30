from flask_restful import Resource

class PessoaController(Resource):

    def get(self):
        return 'Mostrando dados pelo metodo Get'

    def post(self):
        return 'Mostrando Dados pelo metodo Post'

    def put(self):
        return 'Mostrando dados pelo metodo Put'

    def delete(self):
        return 'Mostrando dados pelo metodo Delete'