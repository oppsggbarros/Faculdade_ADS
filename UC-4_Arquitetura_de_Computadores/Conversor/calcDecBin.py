# Calculo de decimal para binario

valor = int(input("Digite um valor decimal: "))
binario = ""
while valor > 0:
    resto = valor % 2
    # print(resto, "valor")
    binario = str(resto) + binario
    # print(binario, "binario")
    valor = valor // 2
    # print(valor, "valor")
print("O valor binário é:", binario)

# Calculo de binario para decimal
valor1 = input("Digite um valor binário: ")
valor2 = 0
for i in range(len(valor1)):
    valor2 += int(valor1[i]) * (2 ** (len(valor1) - i - 1))
print("O valor decimal é:", valor2)