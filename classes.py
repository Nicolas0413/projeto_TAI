class Jogo:
   def __init__(self, nome, desc):
       self.nome = nome
       self.desc = desc


class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.biblioteca = []

    def adicionar_jogo(self):
        self.biblioteca.append(Jogo(input("Digite o nome do jogo: "), input("Digite a descrição do jogo: ")))

    def listar_jogos(self):
        for i in self.biblioteca:
            print(i.nome)

    def remover_jogo(self):
        nome = input("digite o nome do jogo que quer remover: ")
        index = False
        for i in range(1, len(self.biblioteca)):
            if self.biblioteca[i].nome == nome:
                index = i
        if index != False:
            self.biblioteca[i]        
