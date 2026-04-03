# =========================
# CLASSES
# =========================

usuarios = []
jogos = []
reviews = []


class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.biblioteca = []

    def adicionar_usuario(nome, senha):
        for u in usuarios:
            if u.nome == nome:
                return("Usuário já existe.")
                
        usuarios.append(Usuario(nome, senha))
        return("Usuário adicionado.")

    def listar_usuarios():

        if len(usuarios) == 0:
            return("Nenhum usuário cadastrado.")

        return [
            f"Nome: {i.nome} | Senha: {i.senha}"
            for i in usuarios
        ]

    def remover_usuario(nome):

        for i in range(len(usuarios)):
            if usuarios[i].nome == nome:
                usuarios.pop(i)
                return("Usuário removido.")

        return("Usuário não encontrado.")

class Jogo:
    def __init__(self, nome, desc, id):
        self.nome = nome
        self.desc = desc
        self.id = id

    def adicionar_jogo(nome, desc):

        for j in jogos:
            if j.nome == nome:
                return("Jogo já existe.")
                

        jogos.append(Jogo(nome, desc, len(jogos)))
        return("Jogo adicionado.")
    
    def editar_nome(id, nome):
        for j in jogos:
            if j.id == id:
                j.nome = nome
                return("Nome editado com sucesso.")
    
    def editar_desc(id, desc):
        for j in jogos:
            if j.id == id:
                j.desc = desc
                return("Descrição editada com sucesso!")


    def listar_jogos():
        if not jogos:
            return "Não há jogos."

        return [
            f"ID: {i.id} | Nome: {i.nome} | Descrição: {i.desc}"
            for i in jogos
        ]

    def remover_jogo(id):

        for i in range(len(jogos)):
            if jogos[i].id == id:
                jogos.pop(i)
                return("Jogo removido.")

        return("Jogo não encontrado.")
    

class Review:
    def __init__(self, id, nome_usuario, id_jogo, titulo, nota, texto):
        self.id = id
        self.nome_usuario = nome_usuario
        self.id_jogo = id_jogo
        self.titulo = titulo 
        self.nota = nota
        self.texto = texto

    def adicionar_review(nome_usuario, id_jogo, titulo, nota, texto):
        if any(r.nome_usuario == nome_usuario and r.id_jogo == id_jogo for r in reviews):
            return "Esse usuário já realizou uma review desse jogo."
        
        reviews.append(Review(len(reviews), nome_usuario, id_jogo, titulo, nota, texto))
        return("Review adicionada com sucesso")

    def listar_reviews():
        if len(reviews) == 0:
            return("Nenhuma review cadastrada.")

        return [
            {
                "usuario": r.nome_usuario,
                "jogo": next((j.nome for j in jogos if j.id == r.id_jogo), "Jogo não encontrado"),
                "titulo": r.titulo,
                "texto": r.texto,
                "nota": r.nota
            }
            for r in reviews
        ]