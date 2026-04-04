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
        return jsonify({"resultado": resultado}), 201

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
        return jsonify({"resultado": resultado}), 201

    return jsonify({"erro": resultado}), 409

@app.route("/review/add", methods=["POST"])
def post_review():
    usuario_nome = request.json.get("usuario_nome")
    id_jogo = request.json.get("id_jogo")
    titulo = request.json.get("titulo")
    nota = request.json.get("nota")
    texto = request.json.get("texto")

    if not usuario_nome or id_jogo is None or not titulo or nota is None or not texto:
        return jsonify({"erro": "Nome do usuário, Id do jogo, titulo, nota e texto são obrigatórios"}), 400

    resultado = Review.adicionar_review(usuario_nome, id_jogo, titulo, nota, texto)

    if resultado == "Esse usuário já realizou uma review desse jogo.":
        return jsonify({"erro": resultado}), 409

    if resultado == "Esse usuário não existe.":
        return jsonify({"erro": resultado}), 404
    
    if resultado == "Esse jogo não existe.":
        return jsonify({"erro": resultado}), 404
    
    return jsonify({
        "Resultado": resultado
    })


@app.route("/jogo/rmv/<int:id>", methods=["DELETE"])
def delete_jogo(id):
    resultado = Jogo.remover_jogo(id)

    if resultado == "Jogo removido.":
        return jsonify({"resultado": resultado}), 200

    return jsonify({"erro": resultado}), 404

@app.route("/usuario/rmv", methods=["DELETE"])
def delete_usuario():
    nome = request.json.get("nome")
    if nome is None:
        return jsonify({"erro": "Nome é obrigatório"}), 400
    
    resultado = Usuario.remover_usuario(nome)

    if resultado == "Usuário removido.":
        return jsonify({"resultado": resultado}), 200

    return jsonify({"erro": resultado}), 404

@app.route("/jogo/edit/nome/<int:id>", methods=["PUT"])
def edit_jogo_nome(id):
    nome = request.json.get("nome")

    if not nome:
        return jsonify({"erro": "Nome obrigatório"}), 400

    resultado = Jogo.editar_nome_jogo(id, nome)

    if resultado == "Nome editado com sucesso.":
        return jsonify({"resultado": resultado}), 200

    if resultado == "O nome não pode ser o mesmo.":
        return jsonify({"erro": resultado}), 400

    return jsonify({"erro": resultado}), 404

@app.route("/jogo/edit/desc/<int:id>", methods=["PUT"])
def edit_jogo_desc(id):
    desc = request.json.get("desc")

    if not desc:
        return jsonify({"erro": "Descrição obrigatória"}), 400

    resultado = Jogo.editar_desc(id, desc)

    if resultado == "Descrição editada com sucesso!":
        return jsonify({"resultado": resultado}), 200

    if resultado == "A descrição não pode ser a mesma.":
        return jsonify({"erro": resultado}), 400

    return jsonify({"erro": "Jogo não encontrado"}), 404

@app.route("/usuario/edit/nome", methods=["PUT"])
def edit_usuario_nome():
    nome = request.json.get("nome")
    novo = request.json.get("novo")

    if not novo or not nome:
        return jsonify({"erro": "Nome atual e novo são obrigatórios"}), 400

    resultado = Usuario.editar_nome_usuario(nome, novo)

    if resultado == "Nome editado com sucesso.":
        return jsonify({"resultado": resultado}), 200

    if resultado == "O nome não pode ser o mesmo.":
        return jsonify({"erro": resultado}), 400

    return jsonify({"erro": resultado}), 404

@app.route("/usuario/edit/senha", methods=["PUT"])
def edit_senha():
    nome = request.json.get("nome")
    nova = request.json.get("nova")

    if not nova or not nome:
        return jsonify({"erro": "Senha nova e nome atual são obrigatórios"}), 400

    resultado = Usuario.editar_senha(nome, nova)

    if resultado == "Senha editada com sucesso.":
        return jsonify({"resultado": resultado}), 200

    if resultado == "A senha não pode ser a mesma.":
        return jsonify({"erro": resultado}), 400

    return jsonify({"erro": resultado}), 404

@app.route("/jogo/get", methods=["GET"])
def get_jogo():

    jogos = Jogo.listar_jogos()

    if jogos == "Não há jogos.":
        return jsonify({"resultado": "Não há jogos."}), 200

    return jsonify({"jogos": jogos}), 200

@app.route("/usuario/get", methods=["GET"])
def get_usuario():

    return jsonify({
        "usuários": Usuario.listar_usuarios()
    }), 200

@app.route("/review/get", methods=["GET"])
def get_review():

    return jsonify({
        "reviews": Review.listar_reviews()
    }), 200

app.run(debug=True)