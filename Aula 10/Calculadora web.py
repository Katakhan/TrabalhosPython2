
nome_pagina ='calculadora'
from Aula10 import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route ('/')
def init ():
    return render_template('init.html', titulo=nome_pagina)

@app.route ('/calcular')
def calc ():
    n1 =int(request.args['n1'])
    n2 =int(request.args['n2'])
    r_soma = cadicao(n1,n2)
    r_subtracao = csubtracao (n1,n2)
    r_divisao_inteira= cdivisaoint(n1,n2)
    r_divisao_fracionada = cdivisao(n1,n2)
    r_resto = cresto(n1,n2)
    r_raiz = craiz(n1,n2)
    r_multiplicacao = cmultiplicacao(n1,n2)
    resultados = {}
    resultados = {'Resultado da soma':r_soma, 'subtracao':r_subtracao,'multiplicacao':r_multiplicacao, 'divisao_inteira':r_divisao_inteira, 
    'divisao_fracionada':r_divisao_fracionada , 'resto':r_resto, 'raiz':r_raiz }

    return render_template('resultado.html',resultados = resultados)

    # #return render_template ('Resultado.html'
    # ,n1 = n1
    # ,n2 = n2
    # ,soma = r_soma
    # ,subtracao = r_subtracao
    # ,multiplicacao = r_multiplicacao
    # ,divisao_inteira = r_divisao_inteira
    # ,divisao_fracionada = r_divisao_fracionada
    # ,resto = r_resto
    # ,raiz = r_raiz)

app.run ()