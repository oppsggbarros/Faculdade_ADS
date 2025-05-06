# # Calculo de decimal para hexadecimal
# valor = int(input("Digite um valor decimal: "))
# hexadecimal = ""
# while valor > 0:
#     resto = valor % 16
#     if resto < 10:
#         hexadecimal = str(resto) + hexadecimal
#     else:
#         hexadecimal = chr(resto + 55) + hexadecimal
#     valor = valor // 16
# print("O valor hexadecimal é:", hexadecimal)

def decimal_para_hexadecimal(decimal):
    """Converte um número decimal para hexadecimal"""
    try:
        num = int(decimal)
        return hex(num).upper().replace("0X", "0x")
    except ValueError:
        return "Entrada inválida. Por favor, digite um número inteiro."

def hexadecimal_para_decimal(hexadecimal):
    """Converte um número hexadecimal para decimal"""
    try:
        # Remove o prefixo 0x se existir
        hex_clean = hexadecimal.lower().replace("0x", "")
        return int(hex_clean, 16)
    except ValueError:
        return "Entrada inválida. Por favor, digite um número hexadecimal válido."

def main():
    print("Conversor de Decimal para Hexadecimal e Vice-Versa")
    print("1. Decimal para Hexadecimal")
    print("2. Hexadecimal para Decimal")
    
    while True:
        escolha = input("\nEscolha uma opção (1/2) ou 's' para sair: ").strip().lower()
        
        if escolha == 's':
            print("Programa encerrado.")
            break
            
        if escolha == '1':
            decimal = input("Digite o número decimal: ").strip()
            resultado = decimal_para_hexadecimal(decimal)
            print(f"Hexadecimal: {resultado}")
        elif escolha == '2':
            hexadecimal = input("Digite o número hexadecimal (com ou sem 0x): ").strip()
            resultado = hexadecimal_para_decimal(hexadecimal)
            print(f"Decimal: {resultado}")
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()