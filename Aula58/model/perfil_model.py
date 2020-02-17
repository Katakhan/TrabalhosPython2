class Perfil():
    def __init__(self, biografia, interesses, skype, telefone):
        self.biografia = biografia
        self.interesses = interesses
        self.skype = skype
        self.telefone = telefone

    def serialize(self):
        return {
        "biografia": self.biografia,
        "interesses": self.interesses,
        "skype": self.skype,
        "telefone": self.telefone
        }