from classes import Jogo
from classes import Usuario

usuario1 = Usuario("Dudu_games", "senhat0p")


def add_jogo(nome, desc):

    usuario1.adicionar_jogo(nome,desc)

def teste():
    
    return usuario1.listar_jogos()
