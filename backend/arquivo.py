from classes import Jogo
from classes import Usuario
from classes import Review

jogos = Jogo
usuarios = Usuario
reviews = Review

usuarios.adicionar_usuario("Nicolas", "53nh4_1r4d4")
usuarios.adicionar_usuario("Eduardo", "53nh4_M4n31r4")
usuarios.adicionar_usuario("Ignacio", "Melhor professor")
usuarios.adicionar_usuario("Usuario_Legal", "12456")

jogos.adicionar_jogo("Silksong", "Explore, fight and survive as you ascend to the peak of a land ruled by silk and song.")
jogos.adicionar_jogo("PEAK", "PEAK is a co-op climbing game where the slightest mistake can spell your doom.")
jogos.adicionar_jogo("Red Strings Club", "Jogo de bar que questiona questões etícas-filosóficas.")
jogos.adicionar_jogo("Pathologic 2", "Dor e sofrimento.")
jogos.adicionar_jogo("The Binding of Isaac", "Roguelike onde tu chora(literalmente)")

reviews.adicionar_review("Eduardo", 2, "Pérola", 98, "Simplesmente um dos melhores jogos que já joguei na vida.")
reviews.adicionar_review("Eduardo", 3, "Um diamante no mundo dos jogos", 100, "Meu jogo favorito.")
reviews.adicionar_review("Usuario_Legal", 4, "Gosto de jogar", 90, "É um dos mais importantes roguelikes, e sua qualidade reflete nisso.")