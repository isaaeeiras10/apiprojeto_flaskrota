from flask import Flask, jsonify

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
if __name__ == '__main__':
    app.run(debug=True)

