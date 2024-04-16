from flask import Flask, jsonify
from funcoes import *
from random_data import *

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"status": 200, "message": "API da Isabela Canôas da Silva Eiras"})

@app.route("/aleatorios")
def aleatorio():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"ststaus": 200, "data": nome})

@app.route("/maior50")
def maior50():
    return jsonify(maior_de_50(pessoas))

@app.route("/maisde2000")
def maisde2000():
    return jsonify(f'Ganham mais de R$2000 :{mais_2000(pessoas)[0]} pessoas, representando {mais_2000(pessoas)[1]} % de {mais_2000(pessoas)[2]} no total')

@app.route("/tresmaioressalarios")
def tresmaioressalarios():
    return jsonify(maior_salario(pessoas))

@app.route("/mediasalarialprofissao")
def mediasalarialprofissao():
    return jsonify(media_profissoes(pessoas))

@app.route("/maior2000sexo")
def maior2000sexo():
    return jsonify(maior_2000_sexo(pessoas))

if __name__ == '__main__':
    app.run(debug=True)