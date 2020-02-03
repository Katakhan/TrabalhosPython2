from flask_restful import Resource
from flask import request
from TrabalhosPython2.Aula50.Model.enderecomodel import EnderecoModel
from TrabalhosPython2.Aula50.Dao.enderecodao import EnderecoDao


class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        logradouro = request.json['logradouro']
        numero = int(request.json['numero'])
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = int(request.json['cep'])
        endereco = EnderecoModel(logradouro, numero, complemento, bairro, cidade, cep)
        msg = self.dao.insert(endereco)
        return msg

    def put(self):
        logradouro = request.json['logradouro']
        numero = int(request.json['numero'])
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = int(request.json['cep'])
        endereco = EnderecoModel(logradouro, numero, complemento, bairro, cidade, cep)
        msg = self.dao.insert(endereco)
        return msg

    def delete(self, id):
        return self.dao.remove(id)
