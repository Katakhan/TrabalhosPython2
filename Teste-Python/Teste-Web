from flask import Flask
from flask_restful import Api
from Controllers.pessoacontroller import  PessoaController
app= Flask(__name__)
api = Api(app)

api.add_resource( PessoaController, '/api/Pessoa')

@app.route('/')
def inicio():
    return 'Bem vindo a API'

app.run(debug=True, port=80)