from classes import Jogo
from classes import Usuario

jogos = Jogo

Usuario.adicionar_usuario("Nicolas", "53nh4_1r4d4")
Usuario.adicionar_usuario("Eduardo", "53nh4_M4n31r4")

Usuario.listar_usuarios()

jogos.adicionar_jogo("Silksong", "Explore, fight and survive as you ascend to the peak of a land ruled by silk and song.")
jogos.adicionar_jogo("PEAK", "PEAK is a co-op climbing game where the slightest mistake can spell your doom.")

jogos.listar_jogos()

jogos.remover_jogo("PEAK")
jogos.listar_jogos()