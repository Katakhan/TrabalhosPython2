from flask import Flask, render_template
from Faixa import ler
app = Flask(__name__)


@app.route('/lista')
def listar_faixas():
    return render_template("lista.html", nome = 'Lista de Faixas', lista = ler)



app.run()