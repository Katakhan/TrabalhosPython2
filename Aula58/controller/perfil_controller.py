from Aula58.model.perfil_model import Perfil
from Aula58.dao.perfil_dao import PerfilDao

from flask_restful import Resource

class PerfilController(Resource):

    def __init__(self):
        self.dao = PerfilDao()

    def get(self):
        return self.dao.list_all()
