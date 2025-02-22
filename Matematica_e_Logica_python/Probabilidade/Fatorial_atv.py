import math

# 1) Ao jogar um dado, qual a probabilidade de obtermos um número ímpar
# voltado para cima?
# 2) Se lançarmos dois dados ao mesmo tempo, qual a probabilidade de
# dois números iguais carem voltados para cima?
# 3) Um saco contém 8 bolas de mesmo tamanho, mas com cores
# diferentes: três azuis, quatro vermelhas e uma amarela. Retira-se ao
# acaso uma bola. Qual a probabilidade da bola retirada ser azul?
# 4) Qual a probabilidade de tirar um ás ao retirar ao acaso uma carta de um
# baralho com 52 cartas possuindo quatro naipes (copas, paus, ouros e
# espadas) sendo 1 ás em cada naipe?
# 5) Sorteando-se um número de 1 a 20, qual a probabilidade de que esse
# número seja múltiplo de 2?
# 6) Se uma moeda é lançada 5 vezes, qual a probabilidade de sair "cara" 3
# vezes?
# 7) Em uma experiência aleatória foi lançado duas vezes um dado.
# Considerando que o dado é equilibrado, qual a probabilidade de:
# a) A probabilidade de conseguir no primeiro lançamento o número 5 e
# no segundo o número 4.
# b) A probabilidade de obter em pelo menos um dos lançamentos o
# número 5.
# c) A probabilidade de obter a soma dos lançamentos igual a 5.
# d) A probabilidade de obter a soma dos lançamentos igual ou menor
# que 3.
# 8) Um casal planeja ter cinco lhos e deseja saber a probabilidade de
# serem 3 meninos e 2 meninas. Calcule esta probabilidade.
# 9) Em um grupo de 80 alunos, 50 alunos jogam futebol, 40 alunos jogam
# vôlei e 20 jogam futebol e vôlei. Escolhendo ao acaso um dos alunos,
# qual a probabilidade dele jogar futebol ou vôlei?

#1
probabilidade = math.comb(3, 1) / math.comb(6, 1)
print(f"Probabilidade de obter um número ímpar: {probabilidade*100:.2f}%")
#2

probabilidade = math.comb(6, 1) / math.comb(36, 1)
print(f"Probabilidade de obter dois números iguais: {probabilidade*100:.2f}%")
#3
probabilidade = math.comb(3, 1) / math.comb(8, 1)
print(f"Probabilidade de retirar uma bola azul: {probabilidade*100:.2f}%")
#4
probabilidade = math.comb(4, 1) / math.comb(52, 1)
print(f"Probabilidade de tirar um ás: {probabilidade*100:.2f}%")
#5
probabilidade = math.comb(10, 1) / math.comb(20, 1)
print(f"Probabilidade de sortear um número múltiplo de 2: {probabilidade*100:.2f}%")
#6
n = 5
k = 3
p = 0.5
probabilidade = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
print(f"Probabilidade de obter 'cara' 3 vezes: {probabilidade*100:.2f}%")
#7
#a
probabilidade = (math.comb(1, 1) / math.comb(6, 1)) * (math.comb(1, 1) / math.comb(6, 1))
print(f"Probabilidade de obter 5 no primeiro e 4 no segundo: {probabilidade*100:.2f}%")
#b

probabilidade = 1 - ((math.comb(5, 1) / math.comb(6, 1)) * (math.comb(5, 1) / math.comb(6, 1)))
print(f"Probabilidade de obter pelo menos um 5: {probabilidade*100:.2f}%")
#c

probabilidade = math.comb(4, 1) / math.comb(36, 1)
print(f"Probabilidade de obter soma 5: {probabilidade*100:.2f}%")
#d

probabilidade = math.comb(3, 1) / math.comb(36, 1)
print(f"Probabilidade de obter soma igual ou menor que 3: {probabilidade*100:.2f}%")
#8
#sepa ta errada
n = 5
k = 3
p = 0.5
probabilidade = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
print(f"Probabilidade de ter 3 meninos e 2 meninas: {probabilidade*100:.2f}%")
#9

probabilidade = (math.comb(50, 1) / math.comb(80, 1)) + (math.comb(40, 1) / math.comb(80, 1)) - (math.comb(20, 1) / math.comb(80, 1))
print(f"Probabilidade de jogar futebol ou vôlei: {probabilidade*100:.2f}%")
