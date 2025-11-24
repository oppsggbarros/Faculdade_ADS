class Pessoa:
    def __init__(self, nome, telefone=None, email=None, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email
        }

    def __str__(self):
        return f"{self.nome} (id={self.id})"