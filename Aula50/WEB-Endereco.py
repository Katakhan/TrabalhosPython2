from flask import Flask
from flask_restful import Api
from TrabalhosPython2.Aula50.Controllers.enderecocontroller import EnderecoController

app = Flask(__name__)
api = Api(app)

api.add_resource(EnderecoController, '/api/endereco')


@app.route('/')
def inicio():
    return 'Bem vindo a API'


app.run(debug=True, port=70)
