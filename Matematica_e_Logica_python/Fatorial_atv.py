import math
#Uma equipe de trabalho é formada por 6 mulheres e 5 homens. Eles pretendem se organizar em grupo de 6 pessoas, com 4 mulheres e 2 homens, para compor uma comissão. Quantas comissões podem ser formadas?
mulheres = math.comb(6,4)
homens = math.comb(5,2)
comissoes = mulheres * homens
print(comissoes)
# O tênis é um esporte em que a estratégia de jogo a ser adotada depende, entre outros fatores, de o adversário ser canhoto ou destro. Um clube tem um grupo de 10 tenistas, sendo que 4 são canhotos e 6 são destros. O técnico do clube deseja realizar uma partida de exibição entre dois desses jogadores, porém, não poderão ser ambos canhotos. Qual o número de possibilidades de escolha dos tenistas para a partida de exibição?
canhotos = math.comb(4,1)
destros = math.comb(6,1)
partida = canhotos * destros
print(partida)