from utils import carregar_arquivo

clientes = carregar_arquivo("./database/clientes.txt")
reservas = carregar_arquivo("./database/reservas.txt")
pagamentos = carregar_arquivo("./database/pagamentos.txt")

quartos = [
    {"numero": 101, "andar": 1, "status": "Livre"},
    {"numero": 102, "andar": 1, "status": "Livre"},
    {"numero": 201, "andar": 2, "status": "Livre"},
    {"numero": 202, "andar": 2, "status": "Livre"},
]
