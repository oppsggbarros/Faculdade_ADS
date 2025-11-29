from datetime import datetime
from utils import obter_entrada, salvar_arquivo
from data_manager import reservas, pagamentos

def pagamento_reserva():
    print("\nPagamento de Reserva")

    if not reservas:
        print("Nenhuma reserva registrada.")
        return

    for r in reservas:
        print(f"{r['id']} - {r['cliente']['nome']} - {r['status']}")

    id_reserva = obter_entrada("ID da reserva: ", tipo=int)
    reserva = next((r for r in reservas if r["id"] == id_reserva), None)

    if not reserva:
        print("Reserva não encontrada.")
        return

    valor = obter_entrada("Valor: ", tipo=float)

    pagamento = {
        "id": len(pagamentos) + 1,
        "reserva_id": reserva["id"],
        "cliente": reserva["cliente"]["nome"],
        "valor": valor,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    pagamentos.append(pagamento)
    salvar_arquivo("./database/pagamentos.txt", pagamentos)

    print("Pagamento registrado!")
