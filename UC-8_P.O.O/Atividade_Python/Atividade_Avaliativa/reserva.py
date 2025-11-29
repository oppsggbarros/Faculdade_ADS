from utils import obter_entrada, salvar_arquivo
from data_manager import clientes, reservas, quartos

def reservar_quarto():
    print("\nReserva de Quarto")

    if not clientes:
        print("Não há clientes cadastrados.")
        return

    for c in clientes:
        print(f"{c['id']} - {c['nome']}")

    id_cliente = obter_entrada("ID do cliente: ", tipo=int)
    cliente = next((c for c in clientes if c["id"] == id_cliente), None)

    if not cliente:
        print("Cliente não encontrado.")
        return

    quartos_livres = [q for q in quartos if q["status"] == "Livre"]

    if not quartos_livres:
        print("Não há quartos disponíveis.")
        return

    print("\nQuartos Livres:")
    for q in quartos_livres:
        print(f"Quarto {q['numero']} - Andar {q['andar']}")

    numero_quarto = obter_entrada("Número do quarto: ", tipo=int)
    quarto = next((q for q in quartos if q["numero"] == numero_quarto), None)

    if not quarto or quarto["status"] != "Livre":
        print("Quarto indisponível.")
        return

    data = obter_entrada("Data da reserva (dd/mm/aaaa): ")

    reserva = {
        "id": len(reservas) + 1,
        "cliente": {"id": cliente["id"], "nome": cliente["nome"]},
        "quarto": {"numero": quarto["numero"], "andar": quarto["andar"]},
        "data": data,
        "status": "Reservado"
    }

    reservas.append(reserva)
    quarto["status"] = "Ocupado"
    salvar_arquivo("./database/reservas.txt", reservas)

    print("Reserva concluída!")


def check_out():
    print("\nCheck-out")

    reservas_ativas = [r for r in reservas if r["status"] == "Reservado"]

    if not reservas_ativas:
        print("Nenhuma reserva ativa.")
        return

    for r in reservas_ativas:
        print(f"{r['id']} - {r['cliente']['nome']} - Quarto {r['quarto']['numero']}")

    id_reserva = obter_entrada("ID da reserva: ", tipo=int)
    reserva = next((r for r in reservas_ativas if r["id"] == id_reserva), None)

    if not reserva:
        print("Reserva não encontrada.")
        return

    reserva["status"] = "Finalizado"

    numero_quarto = reserva["quarto"]["numero"]
    quarto = next((q for q in quartos if q["numero"] == numero_quarto), None)

    if quarto:
        quarto["status"] = "Livre"

    salvar_arquivo("./database/reservas.txt", reservas)

    print("Check-out realizado!")
