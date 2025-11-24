import os
from datetime import datetime

def salvar_arquivo(nome_arquivo, lista_dados):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for d in lista_dados:
            f.write(str(d) + "\n")


def carregar_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []

    lista = []
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f.readlines():
            linha = linha.strip()
            if linha:
                lista.append(eval(linha))
    return lista

clientes = carregar_arquivo("clientes.txt")
reservas = carregar_arquivo("reservas.txt")
pagamentos = carregar_arquivo("pagamentos.txt")


quartos = [
    {"numero": 101, "andar": 1, "status": "Livre"},
    {"numero": 102, "andar": 1, "status": "Livre"},
    {"numero": 201, "andar": 2, "status": "Livre"},
    {"numero": 202, "andar": 2, "status": "Livre"}
]

def cadastrar_cliente():
    print("\nCdastrar Cliente")
    id = len(clientes) + 1
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    cliente = {
        "id": id,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco
    }

    clientes.append(cliente)
    salvar_arquivo("clientes.txt", clientes)
    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    print("\nCadastros")
    for c in clientes:
        print(f"{c['id']} - {c['nome']} - CPF: {c['cpf']}")


def reservar_quarto():
    print("\nReseva Hotel")
    listar_clientes()

    id_cliente = int(input("ID do cliente: "))

    cliente = next((c for c in clientes if c["id"] == id_cliente), None)
    if not cliente:
        print("Cliente não encontrado.")
        return

    print("\nQuartos disponíveis:")
    for q in quartos:
        if q["status"] == "Livre":
            print(f"Quarto {q['numero']} - Andar {q['andar']}")

    numero_quarto = int(input("\nNúmero do quarto desejado: "))
    quarto = next((q for q in quartos if q["numero"] == numero_quarto), None)

    if not quarto or quarto["status"] != "Livre":
        print("Quarto indisponível.")
        return

    data = input("Data da reserva (dd/mm/aaaa): ")

    reserva = {
        "id": len(reservas) + 1,
        "cliente": cliente,
        "quarto": quarto,
        "data": data,
        "status": "Reservado"
    }

    reservas.append(reserva)
    quarto["status"] = "Ocupado"

    salvar_arquivo("reservas.txt", reservas)

    print("Reserva concluída!")


def check_out():
    print("\nCheck out")

    for r in reservas:
        print(f"{r['id']} - {r['cliente']['nome']} - Quarto {r['quarto']['numero']} - {r['status']}")

    id_reserva = int(input("ID da reserva para check-out: "))

    reserva = next((r for r in reservas if r["id"] == id_reserva), None)
    if not reserva:
        print("Reserva não encontrada.")
        return

    reserva["status"] = "Finalizado"

    numero = reserva["quarto"]["numero"]
    quarto = next((q for q in quartos if q["numero"] == numero), None)
    quarto["status"] = "Livre"

    salvar_arquivo("reservas.txt", reservas)

    print("Check-out realizado com sucesso!")


def pagamento_reserva():
    print("\nPagar Reserva")

    for r in reservas:
        print(f"{r['id']} - {r['cliente']['nome']} - Status: {r['status']}")

    id_reserva = int(input("ID da reserva: "))

    reserva = next((r for r in reservas if r["id"] == id_reserva), None)
    if not reserva:
        print("Reserva não encontrada.")
        return

    valor = float(input("Valor a pagar: "))

    pagamento = {
        "id": len(pagamentos) + 1,
        "cliente": reserva["cliente"]["nome"],
        "valor": valor,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    pagamentos.append(pagamento)
    salvar_arquivo("pagamentos.txt", pagamentos)

    print("Pagamento registrado!")

def menu():
    while True:
        print("SISTEMA DO HOTEL\n")
        print("[1] Cadastrar Cliente")
        print("[2] Listar Clientes")
        print("[3] Reservar Quarto")
        print("[4] Check-out")
        print("[5] Registrar Pagamento")
        print("[0] Sair")

        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_cliente()
        elif opc == "2":
            listar_clientes()
        elif opc == "3":
            reservar_quarto()
        elif opc == "4":
            check_out()
        elif opc == "5":
            pagamento_reserva()
        elif opc == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")


menu()
