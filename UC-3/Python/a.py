# a =""
# for i in range(1,21):
#     a = a + str(i) + " "
#     print(i)
# print(a)

# num1, num2, num3, num4, num5 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: ")), int(input("Digite o quarto número: ")), int(input("Digite o quinto número: "))
# soma = num1 + num2 + num3 + num4 + num5
# media = soma / 5
# print("A soma dos números é:", soma, "e a média é:", media)

n = int(input("Digite um número de elementos: "))
soma = 0
menor = float('inf')
maior = float('-inf')
for i in range(n):
    num = int(input("Digite um número: "))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    soma += num
print("O maior número é:", maior)
print("O menor número é:", menor)
print("A soma do maior e menor número é:", soma)