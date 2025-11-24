from models.pessoa import Pessoa
class Veterinario(Pessoa):
    def __init__(self, nome, especialidade, crm, telefone=None, email=None, id=None):
        super().__init__(nome, telefone, email, id)
        self.especialidade = especialidade
        self.crm = crm


def to_dict(self):
    d = super().to_dict()
    d.update({'especialidade': self.especialidade, 'crm': self.crm})
    return d