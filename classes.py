class Jogo:
   def __init__(self, nome, desc):
       self.nome = nome
       self.desc = desc


class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.biblioteca = []

    def adicionar_jogo(self, nome, desc):
        self.biblioteca.append(Jogo(nome, desc))

    def listar_jogos(self):
        listaJogos = []
        for i in self.biblioteca:
            listaJogos.append(i.nome)
        return listaJogos

    def remover_jogo(self): # não funciona ainda
        nome = input("digite o nome do jogo que quer remover: ")
        index = False
        for i in range(1, len(self.biblioteca)):
            if self.biblioteca[i].nome == nome:
                index = i
        if index != False:
            self.biblioteca[i]        
