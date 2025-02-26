import math

print(" 1. Quantos anagramas diferentes podem ser formados com as letras da palavra ALGORITMO?")

palavra = "ALGORITMO"
n = len(palavra)
anagramas = math.factorial(n)
print("R:", anagramas)
print("2. De quantas formas é possível reorganizar as letras da palavra PROBABILIDADE, considerando as repetições?")

palavra = "PROBABILIDADE"
n = len(palavra)
repetições = {'A': 2, 'B': 2, 'I': 2, 'D': 2}
denominador = 1
for letra, rep in repetições.items():
    denominador *= math.factorial(rep)
anagramas = math.factorial(n) // denominador
print("R:", anagramas)
print(" 3. De quantas maneiras podemos organizar as letras da palavra PITHON, sabendo que as vogais devem estar sempre juntas?")

palavra = "PITHON"
vogais = "IO"
consoantes = "PTHN"
bloco_vogal = 1 
total_blocos = len(consoantes) + bloco_vogal
permutacoes_blocos = math.factorial(total_blocos)
permutacoes_vogais = math.factorial(len(vogais))
total = permutacoes_blocos * permutacoes_vogais
print("R:", total)
print("4. Uma equipe de TI com 10 programadores precisa formar um grupo de 4 pessoas para um projeto especial. De quantas formas diferentes esse grupo pode ser escolhido?")

n = 10
k = 4
combinacoes = math.comb(n, k)
print("R:", combinacoes)
print("5. Em um time de 8 analistas de sistemas e 5 programadores, deseja-se formar um grupo de 5 pessoas, onde pelo menos 2 devem ser programadores. Quantas formações diferentes são possíveis?")

analistas = 8
programadores = 5
total = 0

for p in range(2, 6):
    a = 5 - p
    if a >= 0 and a <= 8:
        total += math.comb(programadores, p) * math.comb(analistas, a)


resp = math.comb(programadores,2) * math.comb(analistas, 3)  + math.comb(programadores,3) * math.comb(analistas, 2) + math.comb(programadores, 4) * math.comb(analistas, 1) + math.comb(programadores, 5) * math.comb(analistas, 0)


print("Resp:", resp)
print(" 6. Um baralho tem 52 cartas. Se uma carta for retirada ao acaso, qual a probabilidade de ela ser uma carta de copas?")

probabilidade = 13 / 52
print("R:", round(probabilidade*100), "%")
print(" 7. Um dado de 6 faces é lançado. Qual a probabilidade de sair um número ímpar?")

probabilidade = 3 / 6
print("R:", round(probabilidade * 100), "%")
print("8. Em uma sala há 30 alunos, dos quais 18 usam óculos. Se um aluno for escolhido aleatoriamente, qual a probabilidade de ele usar óculos?")

probabilidade = 18 / 30
print("R:", round(probabilidade * 100), "%")
print("9. Uma empresa de software tem 60% de funcionários que sabem Python. Entre os que sabem Python, 80% também sabem JavaScript. Se escolhermos um funcionário que sabe JavaScript, qual a probabilidade de ele também saber Python?")

P_Python = 0.6
P_JS_dado_Python = 0.8
P_JS = P_Python * P_JS_dado_Python + (1 - P_Python) * 0 
P_Python_dado_JS = (P_Python * P_JS_dado_Python) / P_JS
print("R:", round(P_Python_dado_JS * 100), "%")
