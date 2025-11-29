import os
import re
from utils import obter_entrada, salvar_arquivo
from data_manager import clientes

DB_DIR = "./UC-8_P.O.O/Atividade_Python/Atividade_Avaliativa/database"
DB_FILE = os.path.join(DB_DIR, "clientes.txt")

def cadastrar_cliente():
    os.makedirs(DB_DIR, exist_ok=True)

    print("\nCadastro de Cliente")
    try:
        id_cliente = max((c.get("id", 0) for c in clientes), default=0) + 1

        nome = obter_entrada("Nome: ").strip()
        if not nome:
            print("Nome é obrigatório.")
            return

        cpf_raw = obter_entrada("CPF (somente números): ").strip()
        cpf_digits = re.sub(r"\D", "", cpf_raw)
        if not cpf_digits:
            print("CPF inválido. Digite apenas números.")
            return

        if len(cpf_digits) not in (11,):
            print("CPF deve conter 11 dígitos.")
            return

        try:
            cpf_int = int(cpf_digits)
        except ValueError:
            print("CPF inválido.")
            return
        
        if any(c.get("cpf") == cpf_int for c in clientes):
            print("CPF já cadastrado.")
            return

        telefone = obter_entrada("Telefone: ", pode_ser_vazio=True)
        endereco = obter_entrada("Endereço: ", pode_ser_vazio=True)

        cliente = {
            "id": id_cliente,
            "nome": nome,
            "cpf": cpf_int,
            "telefone": telefone,
            "endereco": endereco
        }

        clientes.append(cliente)
        salvar_arquivo(DB_FILE, clientes)

        print("Cliente cadastrado com sucesso!")

    except Exception as e:

        print("Ocorreu um erro inesperado ao cadastrar o cliente:")
        print(type(e).__name__, "-", e)



def listar_clientes():
    print("\nClientes Cadastrados:")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for c in clientes:
        print(f"{c['id']} - {c['nome']} - CPF: {c['cpf']}")
