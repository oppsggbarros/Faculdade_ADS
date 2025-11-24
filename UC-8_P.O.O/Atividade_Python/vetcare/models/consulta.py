from datetime import datetime

class Consulta:
    def __init__(self, tutor_id, veterinario_id, nome_animal, data_consulta=None, descricao=None, prescricao_id=None, id=None):
        self.id = id
        self.tutor_id = tutor_id
        self.veterinario_id = veterinario_id
        self.nome_animal = nome_animal
        self.data_consulta = data_consulta or datetime.now()
        self.descricao = descricao
        self.prescricao_id = prescricao_id

def to_row(self):
    return (self.tutor_id, self.veterinario_id, self.nome_animal, self.data_consulta, self.descricao, self.prescricao_id)

def to_dict(self):
    return {
    'id': self.id,
    'tutor_id': self.tutor_id,
    'veterinario_id': self.veterinario_id,
    'nome_animal': self.nome_animal,
    'data_consulta': self.data_consulta,
    'descricao': self.descricao,
    'prescricao_id': self.prescricao_id
}