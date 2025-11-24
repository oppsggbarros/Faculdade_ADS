import json

class Prescricao:
    def __init__(self, descricao, medicamentos=None, id=None):
        self.id = id
        self.descricao = descricao
        self.medicamentos = medicamentos or []

def to_row(self):
    return (self.descricao, json.dumps(self.medicamentos))

def to_dict(self):
    return {'id': self.id, 'descricao': self.descricao, 'medicamentos': self.medicamentos}