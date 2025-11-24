from models.pessoa import Pessoa

class Tutor(Pessoa):
    def __init__(self, nome, endereco, telefone=None, email=None, id=None):
        super().__init__(nome, telefone, email, id)
        self.endereco = endereco
        
def to_dict(self):
    d = super().to_dict()
    d.update({'endereco': self.endereco})
    return d
