import sys
sys.path.append(r'\Users\900132\Desktop\GitHub\TrabalhosPython2\Aula58\controller\perfil_controller.py')

from flask_restful import Api
from flask import Flask

from Aula58.controller.perfil_controller import PerfilController

app = Flask(__name__)
api = Api(app)

api.add_resource(PerfilController, '/api/perfil')

app.run(debug=True)