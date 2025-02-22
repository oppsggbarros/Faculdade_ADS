import math
# Numa certa região, a probabilidade de chover em um dia qualquer é de 0,1. Um meteorologista da tv acerta suas previsões em 80 dos dias em chove e em 90% dos dias em que não chove.
# a)Qual a probabilidade de o meteorologista acertar a previsão de chuva?
# b)Se houver acerto na previsão feita, qual a probabilidade de ter sido um dia de chuva?

P_C = 0.1  # Probabilidade de chover
P_neg_C = 0.9  # Probabilidade de não chover
P_A_given_C = 0.8  # Probabilidade de acerto se chover
P_A_given_neg_C = 0.9  # Probabilidade de acerto se não chover

# a) 
P_A = P_A_given_C * P_C + P_A_given_neg_C * P_neg_C

# b) 
P_C_given_A = (P_A_given_C * P_C) / P_A

# Exibindo os resultados
print(f"Probabilidade de o meteorologista acertar a previsão de chuva: {P_A:.4f}")
print(f"Probabilidade de ter sido um dia de chuva, dado que a previsão foi acertada: {P_C_given_A:.4f}")
