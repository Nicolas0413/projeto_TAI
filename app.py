from flask import Flask, request, jsonify
from classes import Jogo
from classes import Usuario
import arquivo
from classes import jogos
from classes import Review
from classes import reviews

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
        "Resultado": resultado
    })

@app.route("/usuario/add", methods=["POST"])
def post_usuario():
    data = request.json

    nome = data.get("nome")
    senha = data.get("senha")

    if not nome or not senha:
        return jsonify({"erro": "Nome e senha são obrigatórios"}), 400

    resultado = Usuario.adicionar_usuario(nome, senha)

    return jsonify({
        "Resultado": resultado
    })

"""@app.route("/review/add", methods=["POST"])
def post_review():
    usuario_nome = request.json("usuario_nome")
    id_jogo = request.son("id_jogo")
    titulo = request.son("titulo")
    nota = request.son("nota")
    texto = request.son("texto")

    if not usuario_nome or not id_jogo or not titulo or not nota or not texto:
        return jsonify({"erro": "Nome do usuário, Id do jogo, titulo, nota e texto são obrigatórios"}), 400

    resultado = Review.adicionar_usuario(usuario_nome, id_jogo, titulo, nota, texto)

    return jsonify({
        "Resultado": resultado
    })"""

@app.route("/jogo/rmv/<int:id>", methods=["DELETE"])
def delete_jogo(id):
    resultado = Jogo.remover_jogo(id)

    return jsonify({
        "Resultado": resultado if resultado else "Erro, jogo não foi removido."
    })

@app.route("/usuario/rmv/<string:nome>", methods=["DELETE"])
def delete_usuario(nome):
    resultado = Usuario.remover_usuario(nome)

    return jsonify({
        "Resultado": resultado if resultado else "Erro, usuario não foi removido."
    })

@app.route("/jogo/edit/nome/<int:id>", methods=["PUT"])
def edit_jogo_nome(id):
    nome = request.json["nome"]
    resultado = Jogo.editar_nome(id, nome)

    return jsonify({
        "Resultado": resultado if resultado else "Erro, o nome não foi alterado."
    })

@app.route("/jogo/edit/desc/<int:id>", methods=["PUT"])
def edit_jogo_desc(id):
    desc = request.json["desc"]
    resultado = Jogo.editar_desc(id, desc)

    return jsonify({
        "Resultado": resultado if resultado else "erro, a descrição não foi alterada."
    })

@app.route("/jogo/get", methods=["GET"])
def get_jogo():

    return jsonify({
        "jogos": Jogo.listar_jogos()
    })

@app.route("/usuario/get", methods=["GET"])
def get_usuario():

    return jsonify({
        "usuários": Usuario.listar_usuarios()
    })

app.run(debug=True)