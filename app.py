from flask import Flask
from flask import request
from classes import Jogo
from classes import Usuario
import arquivo

app = Flask("meu site legal")

@app.route("/jogo/add", methods=["POST"])
def post_jogo():
    nome = request.json["nome"]
    desc = request.json["desc"]
    arquivo.add_jogo(nome, desc)
    return arquivo.teste()

@app.route("/jogo/rmv/<int:id>", methods=["DELETE"])
def delete_jogo(id):
    rmv_jogo()
    return "Pessoa deletada com sucesso", arquivo.teste()

app.run()
# curl -X POST http://127.0.0.1:5000/jogo/add -H "Content-Type: application/json" -d "{\"nome\":\"Mario\",\"desc\":\"Odissey\"}"
