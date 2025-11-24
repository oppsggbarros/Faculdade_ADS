"""
1. Crie uma classe que modele uma pessoa
(a) Atributos: nome, idade e endereço
(b) Métodos: mostrar endereço e alterar endereço
"""

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def mostrar_endereco(self):
        return self.endereco
    
    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}"


"""
2. Crie uma classe que modele uma aluno
(a) Atributos: nome, numero de matrícula e curso
(b) Métodos: mostrar curso e alterar curso
"""

class Aluno:
    def __init__(self, nome, numero_matricula, curso):
        self.nome = nome
        self.numero_matricula = numero_matricula
        self.curso = curso
    
    def mostrar_curso(self):
        return self.curso
    
    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
    
    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.numero_matricula}, Curso: {self.curso}"


"""
3. Crie uma classe representando os alunos de um determinado curso. A classe deve
conter os atributos matrícula do aluno, nome, nota da primeira prova, nota da segunda
prova e nota da terceira prova. Crie métodos para acessar o nome e a média do aluno.
(a) Permita ao usuario entrar com os dados de 5 alunos.
(b) Encontre o aluno com maior media geral.
(c) Encontre o aluno com menor media geral
(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
aprovacao.
"""

class AlunoCurso:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def get_nome(self):
        return self.nome
    
    def get_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
    
    def situacao(self):
        return "Aprovado" if self.get_media() >= 6 else "Reprovado"
    
    def __str__(self):
        return f"Matrícula: {self.matricula}, Nome: {self.nome}, Média: {self.get_media():.2f}"

def exercicio3():
    alunos = []
    
    print("\n" + "="*50)
    print("EXERCÍCIO 3 - Cadastro de Alunos")
    print("="*50)
    
    print("Digite os dados de 5 alunos:")
    for i in range(5):
        print(f"\nAluno {i+1}:")
        nome = input("Nome: ")
        matricula = input("Matrícula: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        
        aluno = AlunoCurso(matricula, nome, nota1, nota2, nota3)
        alunos.append(aluno)
    
    # Encontrar aluno com maior e menor média
    aluno_maior_media = max(alunos, key=lambda x: x.get_media())
    aluno_menor_media = min(alunos, key=lambda x: x.get_media())
    
    print(f"\nRESULTADOS:")
    print(f"Aluno com maior média: {aluno_maior_media.get_nome()} - Média: {aluno_maior_media.get_media():.2f}")
    print(f"Aluno com menor média: {aluno_menor_media.get_nome()} - Média: {aluno_menor_media.get_media():.2f}")
    
    print("\nSITUAÇÃO DOS ALUNOS:")
    for aluno in alunos:
        print(f"{aluno.get_nome()}: Média {aluno.get_media():.2f} - {aluno.situacao()}")


"""
4. Crie uma classe para representar um numero complexo. Implemente, usando sobrecarga
de operador, os métodos para fazer as operações de soma, subtracao e produto entre
dois numeros.
"""

class NumeroComplexo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
    
    def __add__(self, outro):
        return NumeroComplexo(self.real + outro.real, self.imaginario + outro.imaginario)
    
    def __sub__(self, outro):
        return NumeroComplexo(self.real - outro.real, self.imaginario - outro.imaginario)
    
    def __mul__(self, outro):
        real = self.real * outro.real - self.imaginario * outro.imaginario
        imaginario = self.real * outro.imaginario + self.imaginario * outro.real
        return NumeroComplexo(real, imaginario)
    
    def __str__(self):
        if self.imaginario >= 0:
            return f"{self.real} + {self.imaginario}i"
        else:
            return f"{self.real} - {abs(self.imaginario)}i"


"""
5. Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os
métodos para fazer as operações de incremento (de segundos) no horário e diferença
entre dois horarios.
"""

class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self._normalizar()
    
    def _normalizar(self):
        # Ajusta os valores para ficarem dentro dos limites
        self.minuto += self.segundo // 60
        self.segundo = self.segundo % 60
        
        self.hora += self.minuto // 60
        self.minuto = self.minuto % 60
        
        self.hora = self.hora % 24
    
    def incrementar_segundos(self, segundos):
        self.segundo += segundos
        self._normalizar()
    
    def diferenca(self, outro_horario):
        # Converte ambos para segundos e calcula a diferença
        segundos_self = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        
        diferenca_segundos = abs(segundos_self - segundos_outro)
        
        horas = diferenca_segundos // 3600
        minutos = (diferenca_segundos % 3600) // 60
        segundos = diferenca_segundos % 60
        
        return Horario(horas, minutos, segundos)
    
    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


"""
6. Implemente uma classe para representar em vetor (x,y,z) no R3. Implemente os métodos
para calcular a soma, subtracao, produto vetorial, produto escalar e modulo.
"""

import math

class Vetor3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def soma(self, outro):
        return Vetor3D(self.x + outro.x, self.y + outro.y, self.z + outro.z)
    
    def subtracao(self, outro):
        return Vetor3D(self.x - outro.x, self.y - outro.y, self.z - outro.z)
    
    def produto_escalar(self, outro):
        return self.x * outro.x + self.y * outro.y + self.z * outro.z
    
    def produto_vetorial(self, outro):
        x = self.y * outro.z - self.z * outro.y
        y = self.z * outro.x - self.x * outro.z
        z = self.x * outro.y - self.y * outro.x
        return Vetor3D(x, y, z)
    
    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


"""
7. Crie uma classe que modele um carro
(a) Atributos: marca, ano e preço
(b) Métodos: mostrar preço e de exibição dos dados
Leia os dados de 5 carros e um valor p, Mostre as informações de todos os carros com
preço menor que p.
"""

class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco
    
    def mostrar_preco(self):
        return self.preco
    
    def exibir_dados(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, Preço: R$ {self.preco:.2f}"
    
    def __str__(self):
        return self.exibir_dados()

def exercicio7():
    carros = []
    
    print("\n" + "="*50)
    print("EXERCÍCIO 7 - Cadastro de Carros")
    print("="*50)
    
    print("Digite os dados de 5 carros:")
    for i in range(5):
        print(f"\nCarro {i+1}:")
        marca = input("Marca: ")
        ano = int(input("Ano: "))
        preco = float(input("Preço: R$ "))
        
        carro = Carro(marca, ano, preco)
        carros.append(carro)
    
    p = float(input("\nDigite o valor p para filtrar carros: R$ "))
    
    print(f"\nCarros com preço menor que R$ {p:.2f}:")
    encontrados = False
    for carro in carros:
        if carro.preco < p:
            print(carro.exibir_dados())
            encontrados = True
    
    if not encontrados:
        print("Nenhum carro encontrado com preço menor que o valor informado.")


"""
8. Crie uma classe que modele uma conta corrente
(a) Atributos: numero da conta, nome do correntista e saldo
(b) Métodos: alterar nome, depósito e saque; No construtor, saldo é opcional, com valor
default zero e os demais atributos são obrigatórios.
"""

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False
    
    def saque(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False
    
    def __str__(self):
        return f"Conta: {self.numero_conta}, Correntista: {self.nome_correntista}, Saldo: R$ {self.saldo:.2f}"


"""
9. Um racional é qualquer número da forma p/q, sendo p inteiro e q inteiro não nulo. Crie
uma classe para representar um racional e os seguinte métodos:
(a) inverter sinal;
(b) somar dois racionais;
(c) subtrair dois racionais;
(d) produto de dois racionais;
(e) quociente de dois racionais;
"""

class Racional:
    def __init__(self, p, q):
        if q == 0:
            raise ValueError("Denominador não pode ser zero")
        self.p = p
        self.q = q
        self._simplificar()
    
    def _mdc(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def _simplificar(self):
        divisor = self._mdc(abs(self.p), abs(self.q))
        self.p //= divisor
        self.q //= divisor
        
        if self.q < 0:
            self.p = -self.p
            self.q = -self.q
    
    def inverter_sinal(self):
        return Racional(-self.p, self.q)
    
    def somar(self, outro):
        novo_p = self.p * outro.q + outro.p * self.q
        novo_q = self.q * outro.q
        return Racional(novo_p, novo_q)
    
    def subtrair(self, outro):
        novo_p = self.p * outro.q - outro.p * self.q
        novo_q = self.q * outro.q
        return Racional(novo_p, novo_q)
    
    def produto(self, outro):
        novo_p = self.p * outro.p
        novo_q = self.q * outro.q
        return Racional(novo_p, novo_q)
    
    def quociente(self, outro):
        if outro.p == 0:
            raise ValueError("Divisão por zero")
        novo_p = self.p * outro.q
        novo_q = self.q * outro.p
        return Racional(novo_p, novo_q)
    
    def __str__(self):
        return f"{self.p}/{self.q}"


