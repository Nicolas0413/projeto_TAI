from classes import Jogo
from classes import Usuario

usuario1 = Usuario("Dudu_games", "senhat0p")


usuario1.adicionar_jogo("nome","desc")
usuario1.adicionar_jogo("nome2","desc2")
usuario1.adicionar_jogo("nome3","desc3")

print(usuario1.listar_jogos())

usuario1.remover_jogo()

print(usuario1.listar_jogos())

def add_jogo(nome, desc):

    usuario1.adicionar_jogo(nome,desc)

def teste():
    
    return usuario1.listar_jogos()

def rmv_jogo():
    return usuario1.remover_jogo()