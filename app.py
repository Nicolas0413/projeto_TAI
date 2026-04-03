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

    if resultado == "Jogo adicionado.":
        return jsonify({"msg": resultado}), 201

    return jsonify({"erro": resultado}), 409

@app.route("/usuario/add", methods=["POST"])
def post_usuario():
    data = request.json

    nome = data.get("nome")
    senha = data.get("senha")

    if not nome or not senha:
        return jsonify({"erro": "Nome e senha são obrigatórios"}), 400

    resultado = Usuario.adicionar_usuario(nome, senha)

    if resultado == "Usuário adicionado.":
        return jsonify({"msg": resultado}), 201

    return jsonify({"erro": resultado}), 409


@app.route("/jogo/rmv/<int:id>", methods=["DELETE"])
def delete_jogo(id):
    resultado = Jogo.remover_jogo(id)

    if resultado == "Jogo removido.":
        return jsonify({"msg": resultado}), 200;

    return jsonify({"erro": resultado}), 404;

@app.route("/usuario/rmv/<string:nome>", methods=["DELETE"])
def delete_usuario(nome):
    resultado = Usuario.remover_usuario(nome)

    if resultado == "Usuário removido.":
        return jsonify({"msg": resultado}), 200

    return jsonify({"erro": resultado}), 404

@app.route("/jogo/edit/nome/<int:id>", methods=["PUT"])
def edit_jogo_nome(id):
    nome = request.json["nome"]

    if not nome:
        return jsonify({"erro": "Nome obrigatório"}), 400

    resultado = Jogo.editar_nome(id, nome)

    if resultado == "Nome editado com sucesso.":
        return jsonify({"msg": resultado}), 200

    return jsonify({"erro": resultado}), 404

@app.route("/jogo/edit/desc/<int:id>", methods=["PUT"])
def edit_jogo_desc(id):
    desc = request.json["desc"]

    if not desc:
        return jsonify({"erro": "Descrição obrigatória"}), 400

    resultado = Jogo.editar_desc(id, desc)

    if resultado == "Descrição editada com sucesso!":
        return jsonify({"msg": resultado}), 200

    return jsonify({"erro": "Jogo não encontrado"}), 404

@app.route("/jogo/get", methods=["GET"])
def get_jogo():

    jogos = Jogo.listar_jogos()

    if jogos == "Não há jogos.":
        return "", 204

    return jsonify({"jogos": jogos}), 200

@app.route("/usuario/get", methods=["GET"])
def get_usuario():

    return jsonify({
        "usuários": Usuario.listar_usuarios()
    })

app.run(debug=True)



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