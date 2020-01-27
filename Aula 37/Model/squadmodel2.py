from Dao.squadao import SquaDao

class Squad2:
    def __init__(self):
        self.id = 0
        self.nomesquad = ''

    def __str__(self):
        return f'{self.id};{self.descricao};{self.numeropessoas};{self.linguagembackend};{self.frameworkfrontend};{self.nomesquad};'}'