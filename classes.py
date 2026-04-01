# =========================
# CLASSES
# =========================

usuarios = []
jogos = []


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

        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for u in usuarios:
            print(u.nome)

    def remover_usuario(nome):

        for i in range(len(usuarios)):
            if usuarios[i].nome == nome:
                usuarios.pop(i)
                print("Usuário removido.")
                return

        print("Usuário não encontrado.")


class Jogo:
    def __init__(self, nome, desc):
        self.nome = nome
        self.desc = desc

    def adicionar_jogo(nome, desc):

        for j in jogos:
            if j.nome == nome:
                return("Jogo já existe.")
                

        jogos.append(Jogo(nome, desc))
        return("Jogo adicionado.")


    def listar_jogos():

        if not jogos:
            print("Nenhum jogo cadastrado.")
            return

        for j in jogos:
            print(j.nome)


    def remover_jogo(nome):

        for i in range(len(jogos)):
            if jogos[i].nome == nome:
                jogos.pop(i)
                print("Jogo removido.")
                return

        print("Jogo não encontrado.")