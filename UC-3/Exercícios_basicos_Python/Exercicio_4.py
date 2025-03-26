# Crie um programa que receba três valores do usuário.
# Imprima a soma dos dois primeiros multiplicada pelo terceiro.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print((num1+num2)*num3)

# Faça um programa em linguagem Python que converta
# metros para centímetros. 
centimetros = float(input("Digite a metragem em cm: "))
metros = centimetros / 100
print(metros)

# Faça um algoritmo em linguagem Python que o nome,
# idade, sexo, e receba duas notas e calcule a média
# aritmética e mostre o resultado.
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
sexo = str(input("Digite seu sexo: "))
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Nome: {nome}, Idade: {idade}, Sexo: {sexo}, Média: {media}")