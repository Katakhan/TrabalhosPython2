class Squad:
    def __init__(self):
        self.id = 0
        self.descricao = ''
        self.numeropessoas = 0
        self.linguagembackend = ''
        self.frameworkfrontend = ''
        self.nomesquad = ''

    def __str__(self):
        return f'{self.id};{self.descricao};{self.numeropessoas};{self.linguagembackend};{self.frameworkfrontend};{self.nomesquad};'}'