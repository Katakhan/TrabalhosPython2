from flask import Flask
from flask_restful import Api
from TrabalhosPython2.Aula50.Controllers.pessoacontroller import PessoaController

app= Flask(__name__)
api = Api(app)

api.add_resource( PessoaController, '/api/Pessoa', endpoint='pessoas')
api.add_resource( PessoaController, '/api/Pessoa\<int:id>',endpoint='pessoa')

@app.route('/')
def inicio():
    return 'Bem vindo a API'

app.run(debug=True, port=80)