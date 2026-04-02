from flask import Flask, request, jsonify
from classes import Jogo
from classes import Usuario
import arquivo

app = Flask("meu site legal")

@app.route("/jogo/add", methods=["POST"])
def post_jogo():
    data = request.json

    nome = data.get("nome")
    desc = data.get("desc")

    if not nome or not desc:
        return jsonify({"erro": "Nome e descrição são obrigatórios"}), 400

    resultado = Jogo.adicionar_jogo(nome, desc)

    return jsonify({
        "msg": resultado,
        "jogos": Jogo.listar_jogos()
    })


@app.route("/jogo/rmv/<int:id>", methods=["DELETE"])
def delete_jogo(id):
    resultado = Jogo.remover_jogo(id)

    return jsonify({
        "msg": resultado if resultado else "Jogo removido",
        "jogos": Jogo.listar_jogos()
    })

@app.route("/jogo/edit/<int:id>", methods=["PUT"])
def edit_jogo(id):
    nome = request.json["nome"]
    resultado = Jogo.editar_nome(id, nome)

    return jsonify({
        "msg": resultado if resultado else "Nome editado com sucesso!",
        "jogos": Jogo.listar_jogos()
    })
app.run(debug=True)