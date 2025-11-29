from cliente import cadastrar_cliente, listar_clientes
from reserva import reservar_quarto, check_out
from pagamento import pagamento_reserva

def menu():
    while True:
        print("\nSISTEMA DO HOTEL")
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
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
