# Ex 01. Strings
# Escrever um programa na linguagem Python que conte o
# número de palavras em um texto.
# Como entrada, um texto será digitado de forma interativa no
# teclado.
# Como saída será impresso o texto, bem como a quantidade
# de caracteres desse texto
palavra = str(input("Digite uma palavra: "))
print(f"Tem {len(palavra)} letras.")

# Tamanho de strings. Faça um programa que leia 2 strings e
# informe o conteúdo delas seguido do seu comprimento. 
text1 = str(input("Digite a primeira palavra: "))
text2 = str(input("Digite a segunda palavra: "))
print(f"Primeira palavra: {text1} - Tamanho: {len(text1)}")
print(f"Segunda palavra: {text2} - Tamanho: {len(text2)}")

