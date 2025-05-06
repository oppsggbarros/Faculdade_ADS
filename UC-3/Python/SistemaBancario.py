usuarios = []
cpf = []
rg = []
telefone = []
numero_da_agencia = []
numero_da_conta = []
saldo = []
while True:
    print("Sistema Bancário")
    print("1. Cadastrar Usuário")
    print("2. Consultar Saldo")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Transferir")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do usuário: ")
        cpf_usuario = input("Digite o CPF do usuário: ")
        rg_usuario = input("Digite o RG do usuário: ")
        telefone_usuario = input("Digite o telefone do usuário: ")
        numero_agencia = input("Digite o número da agência: ")
        numero_conta = input("Digite o número da conta: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))

        usuarios.append(nome)
        cpf.append(cpf_usuario)
        rg.append(rg_usuario)
        telefone.append(telefone_usuario)
        numero_da_agencia.append(numero_agencia)
        numero_da_conta.append(numero_conta)
        saldo.append(saldo_inicial)

        print(f"Usuário {nome} cadastrado com sucesso!")

    elif opcao == '2':
        nome_consulta = input("Digite o nome do usuário para consultar saldo: ")
        if nome_consulta in usuarios:
            index = usuarios.index(nome_consulta)
            print(f"Saldo de {nome_consulta}: R$ {saldo[index]:.2f}")
        else:
            print("Usuário não encontrado.")

    elif opcao == '3':
        nome_deposito = input("Digite o nome do usuário para depositar: ")
        if nome_deposito in usuarios:
            index = usuarios.index(nome_deposito)
            valor_deposito = float(input(f"Digite o valor a depositar para {nome_deposito}: "))
            saldo[index] += valor_deposito
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            print(f"Novo saldo de {nome_deposito}: R$ {saldo[index]:.2f}")
        else:
            print("Usuário não encontrado.")

    elif opcao == '4':
        nome_saque = input("Digite o nome do usuário para sacar: ")
        if nome_saque in usuarios:
            index = usuarios.index(nome_saque)
            valor_saque = float(input(f"Digite o valor a sacar para {nome_saque}: "))
            if valor_saque <= saldo[index]:
                saldo[index] -= valor_saque
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
                print(f"Novo saldo de {nome_saque}: R$ {saldo[index]:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Usuário não encontrado.")
    elif opcao == '5':
        nome_transferencia = input("Digite o nome do usuário para transferir: ")
        if nome_transferencia in usuarios:
            index = usuarios.index(nome_transferencia)
            valor_transferencia = float(input(f"Digite o valor a transferir para {nome_transferencia}: "))
            if valor_transferencia <= saldo[index]:
                saldo[index] -= valor_transferencia
                print(f"Transferência de R$ {valor_transferencia:.2f} realizada com sucesso!")
                print(f"Novo saldo de {nome_transferencia}: R$ {saldo[index]:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Usuário não encontrado.")
    elif opcao == '6':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")