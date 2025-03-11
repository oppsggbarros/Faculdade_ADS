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

from math import comb

# Exercício 10
def prob_defeito_linha_b():
    prob_A = 0.7
    prob_B = 0.3
    defeito_A = 0.02
    defeito_B = 0.05

    
    prob_defeito_total = (prob_A * defeito_A) + (prob_B * defeito_B)

    prob_B_dado_defeito = (prob_B * defeito_B) / prob_defeito_total
    return prob_B_dado_defeito

# Exercício 11
def prob_matematica_ou_fisica():
    total_estudantes = 100
    matematica = 60
    fisica = 50
    ambas = 30

    prob_matematica_ou_fisica = (matematica + fisica - ambas) / total_estudantes
    return prob_matematica_ou_fisica

# Exercício 12
def prob_pelo_menos_uma_medida():
    senha_forte = 0.7
    autenticacao_dois_fatores = 0.5
    ambas = 0.4

    prob_pelo_menos_uma = senha_forte + autenticacao_dois_fatores - ambas
    return prob_pelo_menos_uma

# Exercício 13
def prob_defeito():
    prob_A = 0.5
    prob_B = 0.3
    prob_C = 0.2
    defeito_A = 0.03
    defeito_B = 0.05
    defeito_C = 0.08

    prob_defeito_total = (prob_A * defeito_A) + (prob_B * defeito_B) + (prob_C * defeito_C)
    return prob_defeito_total

# Exercício 14
def prob_medico2_dado_diagnostico_correto():
    prob_M1 = 0.4
    prob_M2 = 0.35
    prob_M3 = 0.25
    acerto_M1 = 0.9
    acerto_M2 = 0.85
    acerto_M3 = 0.8

    prob_diagnostico_correto = (prob_M1 * acerto_M1) + (prob_M2 * acerto_M2) + (prob_M3 * acerto_M3)

    
    prob_M2_dado_correto = (prob_M2 * acerto_M2) / prob_diagnostico_correto
    return prob_M2_dado_correto

# Exercício 15
def prob_ataque_dado_alerta():
    prob_ataque = 0.01
    prob_detectar_ataque = 0.95
    prob_falso_positivo = 0.05

    prob_alerta = (prob_ataque * prob_detectar_ataque) + ((1 - prob_ataque) * prob_falso_positivo)

    prob_ataque_dado_alerta = (prob_ataque * prob_detectar_ataque) / prob_alerta
    return prob_ataque_dado_alerta

# Exercício 16
def prob_doente_dado_positivo():
    prob_doente = 0.005
    sensibilidade = 0.98
    especificidade = 0.95

    prob_positivo = (prob_doente * sensibilidade) + ((1 - prob_doente) * (1 - especificidade))

    prob_doente_dado_positivo = (prob_doente * sensibilidade) / prob_positivo
    return prob_doente_dado_positivo

# Exercício 17
def prob_exatamente_2_mulheres():
    total_homens = 4
    total_mulheres = 6
    total_pessoas = total_homens + total_mulheres
    escolhidos = 3

    maneiras_2_mulheres = comb(total_mulheres, 2) * comb(total_homens, 1)

    total_maneiras = comb(total_pessoas, escolhidos)

    
    prob_2_mulheres = maneiras_2_mulheres / total_maneiras
    return prob_2_mulheres

# Exercício 18
def prob_todas_vermelhas():
    total_vermelhas = 7
    total_azuis = 5
    total_bolas = total_vermelhas + total_azuis
    escolhidas = 3

    maneiras_3_vermelhas = comb(total_vermelhas, 3)

    total_maneiras = comb(total_bolas, escolhidas)

    prob_3_vermelhas = maneiras_3_vermelhas / total_maneiras
    return prob_3_vermelhas

# Exercício 19
def prob_pelo_menos_2_mulheres():
    total_candidatos = 100
    total_mulheres = 30
    total_homens = 70
    vencedores = 5

    maneiras_pelo_menos_2_mulheres = sum(comb(total_mulheres, k) * comb(total_homens, vencedores - k) for k in range(2, vencedores + 1))

    total_maneiras = comb(total_candidatos, vencedores)

    prob_pelo_menos_2 = maneiras_pelo_menos_2_mulheres / total_maneiras
    return prob_pelo_menos_2

# Exercício 20
def prob_pelo_menos_1_especialista():
    total_candidatos = 10
    especialistas = 4
    nao_especialistas = 6
    contratados = 3

    maneiras_pelo_menos_1_especialista = sum(comb(especialistas, k) * comb(nao_especialistas, contratados - k) for k in range(1, contratados + 1))

    total_maneiras = comb(total_candidatos, contratados)

    prob_pelo_menos_1 = maneiras_pelo_menos_1_especialista / total_maneiras
    return prob_pelo_menos_1

# Resultados
print("Exercício 10:", prob_defeito_linha_b())
print("Exercício 11:", prob_matematica_ou_fisica())
print("Exercício 12:", prob_pelo_menos_uma_medida())
print("Exercício 13:", prob_defeito())
print("Exercício 14:", prob_medico2_dado_diagnostico_correto())
print("Exercício 15:", prob_ataque_dado_alerta())
print("Exercício 16:", prob_doente_dado_positivo())
print("Exercício 17:", prob_exatamente_2_mulheres())
print("Exercício 18:", prob_todas_vermelhas())
print("Exercício 19:", prob_pelo_menos_2_mulheres())
print("Exercício 20:", prob_pelo_menos_1_especialista())