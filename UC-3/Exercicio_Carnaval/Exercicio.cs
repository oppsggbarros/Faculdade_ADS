using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Exercicio_Carnaval
{
    public class Exercicio_pag2
    {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Crie um algoritmo que leia a idade de uma pessoa e diga se ela é maior de idade (18 anos ou mais) ou menor de idade.");
            int idade;
            Console.WriteLine("Qual a sua idade?");
            idade = Convert.ToInt32(Console.ReadLine());
            if (idade >= 18)
            {
                System.Console.WriteLine("É maior idade");
            }
            else
            {
                System.Console.WriteLine("Não é maior idade");
            }

            System.Console.WriteLine("Leia um número e informe se ele é par ou ímpar.");
            int num;
            System.Console.WriteLine("Digite um numero");
            num = Convert.ToInt32(Console.ReadLine());
            if (num % 2 == 0)
            {
                System.Console.WriteLine("O número é par");
            }
            else
            {
                System.Console.WriteLine("O número é impar");
            }

            System.Console.WriteLine("Peça para o usuário informar a sua idade e verifique se ele tem idade para votar (entre 16 e 70 anos).");
            int idade_V;
            System.Console.WriteLine("Qual a sua idade?");
            idade_V = Convert.ToInt32(Console.ReadLine());
            if (idade_V >= 16 && idade_V <=70)
            {
                System.Console.WriteLine("Você pode votar");
            }
            else
            {
                System.Console.WriteLine("Você não pode votar");
            }

            System.Console.WriteLine("Leia um número e informe se ele é positivo, negativo ou zero.");
            int numP_I;
            System.Console.WriteLine("Escreva um número");
            numP_I = Convert.ToInt32(Console.ReadLine());
            if (numP_I < 0)
            {
                System.Console.WriteLine("O número é negativo");
            }
            else if (numP_I == 0)
            {
                System.Console.WriteLine("O número é zero");
            }
            else
            {
                System.Console.WriteLine("É um número positivo");
            }

            System.Console.WriteLine("Crie um algoritmo que leia o valor de uma compra e, se for superior a R$100, aplique um desconto de 10%. Caso contrário, informe que o valor da compra não tem desconto.");
            float valorCompra;
            int valorTotal = 100;
            float desconto;
            System.Console.WriteLine("Digite o valor do produto");
            valorCompra = Convert.ToInt32(Console.ReadLine());
            if (valorCompra > valorTotal)
            {
                desconto = valorCompra * 0.1f;
                System.Console.WriteLine("Teve desconto de 10%");
                System.Console.WriteLine($"A compra teve R${desconto} de desconto");
                System.Console.WriteLine($"Valor total da compra R${valorCompra - desconto}");
            }
            else
            {
                System.Console.WriteLine("Não teve desconto");
            }

            System.Console.WriteLine("Peça ao usuário para digitar a nota de um aluno e, se for maior ou igual a 7, informe que ele está aprovado. Caso contrário, informe que ele está reprovado.");            int nota;
            System.Console.WriteLine("Digite a nota do aluno");
            nota = Convert.ToInt32(Console.ReadLine());
            if (nota >= 7 && nota <= 10)
            {
                System.Console.WriteLine("Aluno aprovado");
            }
            else if (nota >= 0 && nota < 7)
            {
                System.Console.WriteLine("Aluno reprovado");
            }
            else
            {
                System.Console.WriteLine("Nota não válida");
            }

            System.Console.WriteLine("Receba três valores que representam os lados de um triângulo e verifique se eles formam um triângulo válido.");
            int lado1;
            int lado2;
            int lado3;
            System.Console.WriteLine("Digite um numero");
            lado1 = Convert.ToInt32(Console.ReadLine());
            System.Console.WriteLine("Digite outro numero");
            lado2 = Convert.ToInt32(Console.ReadLine());
            System.Console.WriteLine("Digite outro numero");
            lado3 = Convert.ToInt32(Console.ReadLine());
            if (lado1 + lado2 > lado3)
            {
                System.Console.WriteLine("É um triângulo");
            }
            else
            {
                System.Console.WriteLine("Não é um triângulo");
            }

            System.Console.WriteLine("Receba dois números e informe se a soma deles é maior que 10.");
            int num1;
            int num2;
            System.Console.WriteLine("Digite um número");
            num1 = Convert.ToInt32(Console.ReadLine());
            System.Console.WriteLine("Digite outro número");
            num2 = Convert.ToInt32(Console.ReadLine());
            if (num1 + num2 > 10)
            {
                System.Console.WriteLine("O valor é maior que 10");
            }
            else
            {
                System.Console.WriteLine("O valor é menor ou igual a 10");
            }

            System.Console.WriteLine("Leia três números e calcule a média. Se a média for maior que 6, informe (Aprovado), senão, informe (Reprovado).");
            int nota1;
            int nota2;
            int nota3;
            float media;

            System.Console.WriteLine("Informe a primeira nota:");
            nota1 = Convert.ToInt32(Console.ReadLine());
            System.Console.WriteLine("Informe a segunda nota:");
            nota2 = Convert.ToInt32(Console.ReadLine());
            System.Console.WriteLine("Informe a terceira nota:");
            nota3 = Convert.ToInt32(Console.ReadLine());
            media = (nota1 + nota2 + nota3) / 3;
            if (media >= 6 && media <= 10)
            {
                System.Console.WriteLine("Aprovado");
            }
            else if (media >= 0 && media < 6)
            {
                System.Console.WriteLine("Reprovado");
            }
            else
            {
                System.Console.WriteLine("Nota inválida");
            }

            System.Console.WriteLine("Receba dois números e informe qual é o maior.");
            int num_1;
            int num_2;
            System.Console.WriteLine("Digite um número");
            num_1 = Convert.ToInt32(Console.ReadLine());
            System.Console.WriteLine("Digite outro número");
            num_2 = Convert.ToInt32(Console.ReadLine());
            if (num1 > num2)
            {
                System.Console.WriteLine("O primeiro número é maior");
            }
            else if (num2 > num1)
            {
                System.Console.WriteLine("O segundo número é maior");
            }
            else
            {
                System.Console.WriteLine("Os números são iguais");
            }

            System.Console.WriteLine("Peça um ano ao usuário e verifique se ele é bissexto.");
            int ano;
            System.Console.WriteLine("Digite um ano:");
            ano = Convert.ToInt32(Console.ReadLine());
            if (ano % 4 == 0 && (ano % 100 != 0 || ano % 400 == 0))
            {
                System.Console.WriteLine("O ano é bissexto");
            }
            else
            {
                System.Console.WriteLine("O ano não é bissexto");
            }

            System.Console.WriteLine("Leia o preço de um produto e, se ele for maior que R$ 50, acrescente 18% de imposto sobre ele.");
            double preço;
            double total;

            System.Console.WriteLine("Digite o valor do Produto:");
            preço = Convert.ToDouble(Console.ReadLine());
            if (preço > 50)
            {
                total = preço * 1.18f;
                System.Console.WriteLine("O valor total é: " + total);
            }
            else
            {
                System.Console.WriteLine("o valor total é: " + preço);
            }

            System.Console.WriteLine("Receba o peso e a altura de uma pessoa, calcule o IMC e classifique como: abaixo do peso, peso normal, sobrepeso, obesidade, etc");
            double peso;
            double altura;
            double imc;
            System.Console.WriteLine("Informe seu peso:");
            peso = Convert.ToDouble(Console.ReadLine());
            System.Console.WriteLine("Informe sua altura:");
            altura = Convert.ToDouble(Console.ReadLine());
            imc = peso / Math.Pow(altura, 2);
            if (imc < 18.5)
            {
                System.Console.WriteLine("Abaixo do peso");
            }
            else if (imc >= 18.5 && imc < 25)
            {
                System.Console.WriteLine("Peso normal");
            }
            else if (imc >= 25 && imc < 30)
            {
                System.Console.WriteLine("Sobrepeso");
            }
            else
            {
                System.Console.WriteLine("Obesidade");
            }
            // Verificar número de entrada
            Console.Write("Digite um número: ");
            int numero = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(numero > 100 ? "Número grande" : "Número pequeno");

            // Categoria de filme
            Console.Write("Digite a idade: ");
            int idade_a = Convert.ToInt32(Console.ReadLine());
            if (idade <= 12) Console.WriteLine("Infantil");
            else if (idade <= 17) Console.WriteLine("Adolescente");
            else Console.WriteLine("Adulto");

            // Fatorial de um número
            Console.Write("Digite um número: ");
            int num_5 = Convert.ToInt32(Console.ReadLine());
            if (num > 0)
            {
                int fatorial = 1;
                for (int i = 1; i <= num; i++) fatorial *= i;
                Console.WriteLine($"Fatorial: {fatorial}");
            }

            // Verificar salário de empregado
            Console.Write("Digite o salário: ");
            double salario = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(salario > 2000 ? "Tem direito a bônus" : "Não tem direito a bônus");

            // Nota final de aluno
            Console.Write("Digite a nota: ");
            double nota_3 = Convert.ToDouble(Console.ReadLine());
            if (nota > 9) Console.WriteLine("Nota excelente");
            else if (nota > 7) Console.WriteLine("Nota boa");
            else if (nota > 5) Console.WriteLine("Nota regular");
            else Console.WriteLine("Nota ruim");

            // Preço com frete
            Console.Write("Digite o valor da compra: ");
            double compra = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(compra > 200 ? "Frete grátis" : "Frete a ser calculado");

            // Calcular hora extra
            Console.Write("Digite as horas trabalhadas: ");
            int horas = Convert.ToInt32(Console.ReadLine());
            if (horas > 40)
            {
                double valorExtra = (horas - 40) * 1.1;
                Console.WriteLine($"Valor das horas extras: {valorExtra}");
            }

            // Pagamento com juros
            Console.Write("Digite o valor: ");
            double valor = Convert.ToDouble(Console.ReadLine());
            Console.Write("Dias de atraso: ");
            int dias = Convert.ToInt32(Console.ReadLine());
            if (dias > 30) Console.WriteLine($"Valor com juros: {valor * 1.05}");

            // Verificar salário abaixo da média
            Console.Write("Digite o salário: ");
            double sal = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(sal < 1500 ? "Abaixo da média" : "Acima da média");

            // Idade para aposentadoria
            Console.Write("Digite a idade: ");
            int idadeAposentadoria = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(idadeAposentadoria >= 60 ? "Pode se aposentar" : "Não pode se aposentar");

            // Classificação de tempo
            Console.Write("Digite a temperatura: ");
            double temp = Convert.ToDouble(Console.ReadLine());
            if (temp > 30) Console.WriteLine("Muito quente");
            else if (temp > 20) Console.WriteLine("Quente");
            else if (temp > 10) Console.WriteLine("Aconchegante");
            else Console.WriteLine("Frio");

            // Meses do ano
            Console.Write("Digite o número do mês: ");
            int mes = Convert.ToInt32(Console.ReadLine());
            string[] meses = { "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" };
            Console.WriteLine(meses[mes - 1]);

            // Aprovado ou reprovado
            Console.Write("Digite a primeira nota: ");
            double nota_1 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite a segunda nota: ");
            double nota_2 = Convert.ToDouble(Console.ReadLine());
            double media_a = (nota_1 + nota_2) / 2;
            Console.WriteLine(media_a > 6 ? "Aprovado" : "Reprovado");

            // Verificação de múltiplos de 5
            Console.Write("Digite um número: ");
            int num5 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(num5 % 5 == 0 ? "Múltiplo de 5" : "Não é múltiplo de 5");

            // Temperatura em Fahrenheit
            Console.Write("Digite a temperatura em Celsius: ");
            double celsius = Convert.ToDouble(Console.ReadLine());
            double fahrenheit = (celsius * 9 / 5) + 32;
            Console.WriteLine($"Temperatura em Fahrenheit: {fahrenheit}");
            Console.WriteLine(celsius > 30 ? "Calor" : "Frio");

            // Definir idade para ingresso
            Console.Write("Digite a idade: ");
            int idadeIngresso = Convert.ToInt32(Console.ReadLine());
            if (idadeIngresso < 12) Console.WriteLine("Ingresso infantil");
            else if (idadeIngresso <= 18) Console.WriteLine("Ingresso juvenil");
            else Console.WriteLine("Ingresso adulto");

            // Imposto sobre renda
            Console.Write("Digite o salário: ");
            double salarioImposto = Convert.ToDouble(Console.ReadLine());
            if (salarioImposto > 5000) Console.WriteLine($"Imposto: {salarioImposto * 0.15}");

            // Escolha de bebida
            Console.Write("Escolha uma bebida (Coca-Cola, Cerveja, Água): ");
            string bebida = Console.ReadLine();
            switch (bebida)
            {
                case "Coca-Cola": Console.WriteLine("Refrigerante"); break;
                case "Cerveja": Console.WriteLine("Álcool"); break;
                case "Água": Console.WriteLine("Bebida saudável"); break;
            }

            // Calcular desconto no preço
            Console.Write("Digite o preço: ");
            double preco = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(preco > 500 ? $"Preço com desconto: {preco * 0.8}" : $"Preço com desconto: {preco * 0.9}");

            // Verificação de número perfeito
            Console.Write("Digite um número: ");
            int numPerfeito = Convert.ToInt32(Console.ReadLine());
            int somaDivisores = 0;
            for (int i = 1; i < numPerfeito; i++)
            {
                if (numPerfeito % i == 0) somaDivisores += i;
            }
            Console.WriteLine(somaDivisores == numPerfeito ? "Número perfeito" : "Não é número perfeito");

            // Dia da semana
            Console.Write("Digite o número do dia: ");
            int dia = Convert.ToInt32(Console.ReadLine());
            string[] diasSemana = { "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado" };
            Console.WriteLine(diasSemana[dia - 1]);

            // Determinar classe social
            Console.Write("Digite a renda: ");
            double renda = Convert.ToDouble(Console.ReadLine());
            if (renda <= 1500) Console.WriteLine("Classe baixa");
            else if (renda <= 5000) Console.WriteLine("Classe média");
            else Console.WriteLine("Classe alta");

            // Média de idade
            int somaIdades = 0;
            for (int i = 0; i < 5; i++)
            {
                Console.Write($"Digite a idade {i + 1}: ");
                somaIdades += Convert.ToInt32(Console.ReadLine());
            }
            double mediaIdades = somaIdades / 5.0;
            Console.WriteLine(mediaIdades > 30 ? "Média maior que 30" : "Média menor ou igual a 30");

            // Classificação de notas
            Console.Write("Digite a nota: ");
            double notaClassificacao = Convert.ToDouble(Console.ReadLine());
            if (notaClassificacao < 3) Console.WriteLine("Muito Baixa");
            else if (notaClassificacao < 5) Console.WriteLine("Baixa");
            else if (notaClassificacao < 7) Console.WriteLine("Média");
            else if (notaClassificacao < 9) Console.WriteLine("Boa");
            else Console.WriteLine("Excelente");

            // Divisão por 3
            Console.Write("Digite um número: ");
            int numDiv3 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(numDiv3 % 3 == 0 ? "Divisível por 3" : "Não divisível por 3");

            // Cálculo de área de círculo
            Console.Write("Digite o raio: ");
            double raio = Convert.ToDouble(Console.ReadLine());
            if (raio > 5) Console.WriteLine($"Área: {Math.PI * raio * raio}");

            // Resultado de eleição
            Console.Write("Digite os votos do candidato A: ");
            int votosA = Convert.ToInt32(Console.ReadLine());
            Console.Write("Digite os votos do candidato B: ");
            int votosB = Convert.ToInt32(Console.ReadLine());
            if (votosA > votosB) Console.WriteLine("Candidato A venceu");
            else if (votosB > votosA) Console.WriteLine("Candidato B venceu");
            else Console.WriteLine("Empate");

            // Temperatura em Kelvin
            Console.Write("Digite a temperatura em Celsius: ");
            double celsiusKelvin = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine($"Temperatura em Kelvin: {celsiusKelvin + 273.15}");

            // Calcular hora adicional
            Console.Write("Digite as horas extras: ");
            int horasExtras = Convert.ToInt32(Console.ReadLine());
            if (horasExtras > 40) Console.WriteLine($"Valor das horas adicionais: {(horasExtras - 40) * 1.1}");

            // Classificar alimentos
            Console.Write("Digite as calorias: ");
            int calorias = Convert.ToInt32(Console.ReadLine());
            if (calorias < 100) Console.WriteLine("Baixas Calorias");
            else if (calorias < 300) Console.WriteLine("Média Caloria");
            else Console.WriteLine("Alta Caloria");

            // Boleto com multa
            Console.Write("Digite o valor do boleto: ");
            double boleto = Convert.ToDouble(Console.ReadLine());
            Console.Write("Dias de atraso: ");
            int diasAtraso = Convert.ToInt32(Console.ReadLine());
            if (diasAtraso > 0) Console.WriteLine($"Valor com multa: {boleto * 1.02}");

            // Ano de eleição
            Console.Write("Digite o ano: ");
            int ano_e = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(ano_e % 4 == 0 ? "Ano de eleição" : "Não é ano de eleição");

            // Calculadora de descontos
            Console.Write("Digite o valor do produto: ");
            double valorProduto = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(valorProduto > 100 ? $"Preço com desconto: {valorProduto * 0.85}" : $"Preço com desconto: {valorProduto * 0.9}");

            // Valor de combustível
            Console.Write("Digite o valor do combustível: ");
            double combustivel = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(combustivel > 5 ? "Caro" : "Barato");

            // Verificar maior número de três
            Console.Write("Digite o primeiro número: ");
            int num1_max = Convert.ToInt32(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            int num2_max = Convert.ToInt32(Console.ReadLine());
            Console.Write("Digite o terceiro número: ");
            int num3_max = Convert.ToInt32(Console.ReadLine());
            int maior = Math.Max(num1_max, Math.Max(num2_max, num3_max));
            Console.WriteLine($"Maior número: {maior}");

            // Calculadora de IMC
            Console.Write("Digite o peso: ");
            double peso_imc = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite a altura: ");
            double altura_imc = Convert.ToDouble(Console.ReadLine());
            double imc_a = peso_imc / (altura_imc * altura_imc);
            if (imc_a < 18.5) Console.WriteLine("Abaixo do peso");
            else if (imc_a < 25) Console.WriteLine("Peso normal");
            else if (imc_a < 30) Console.WriteLine("Sobrepeso");
            else Console.WriteLine("Obesidade");

            // Lançamento de dados
            Random rand = new Random();
            int dado = rand.Next(1, 7);
            Console.WriteLine($"Número sorteado: {dado}");

            // Definir horário de trabalho
            Console.Write("Digite o horário de entrada (hh:mm): ");
            TimeSpan entrada = TimeSpan.Parse(Console.ReadLine());
            if (entrada < new TimeSpan(9, 0, 0)) Console.WriteLine("Entrada antecipada");
            else if (entrada <= new TimeSpan(12, 0, 0)) Console.WriteLine("Entrada no horário");
            else Console.WriteLine("Entrada tardia");

            // Verificar idade de entrada no cinema
            Console.Write("Digite a idade: ");
            int idadeCinema = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(idadeCinema < 18 ? "Meia-entrada" : "Entrada inteira");

            // Cálculo de aposentadoria
            Console.Write("Digite a idade: ");
            int idadeApos = Convert.ToInt32(Console.ReadLine());
            Console.Write("Digite o tempo de serviço: ");
            int tempoServico = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(idadeApos >= 60 && tempoServico >= 30 ? "Pode se aposentar" : "Não pode se aposentar");

            // Calcular valor de mensalidade escolar
            Console.Write("O aluno é bolsista? (s/n): ");
            char bolsista = Console.ReadLine()[0];
            Console.Write("Digite o valor da mensalidade: ");
            double mensalidade = Convert.ToDouble(Console.ReadLine());
            if (bolsista == 's') Console.WriteLine($"Valor com desconto: {mensalidade * 0.5}");
            else Console.WriteLine($"Valor com desconto: {mensalidade * 0.9}");

            // Soma de números positivos
            Console.Write("Digite o primeiro número: ");
            int numPos1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            int numPos2 = Convert.ToInt32(Console.ReadLine());
            if (numPos1 > 0 && numPos2 > 0) Console.WriteLine($"Soma: {numPos1 + numPos2}");
            else Console.WriteLine("A soma não pode ser realizada");

            // Verificar estudante universitário
            Console.Write("É estudante universitário? (s/n): ");
            char estudante = Console.ReadLine()[0];
            Console.WriteLine(estudante == 's' ? "Tem direito a desconto" : "Não tem direito a desconto");

            // Idade para cadastro de usuário
            Console.Write("Digite a idade: ");
            int idadeCadastro = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(idadeCadastro >= 18 ? "Cadastro permitido" : "Cadastro restrito a maiores de 18");

            // Valor do imposto de renda
            Console.Write("Digite o salário: ");
            double salarioIR = Convert.ToDouble(Console.ReadLine());
            if (salarioIR > 4000) Console.WriteLine($"Imposto: {salarioIR * 0.1}");

            // Resultado do jogo de futebol
            Console.Write("Digite os gols do time A: ");
            int golsA = Convert.ToInt32(Console.ReadLine());
            Console.Write("Digite os gols do time B: ");
            int golsB = Convert.ToInt32(Console.ReadLine());
            if (golsA > golsB) Console.WriteLine("Time A venceu");
            else if (golsB > golsA) Console.WriteLine("Time B venceu");
            else Console.WriteLine("Empate");

            // Verificação de idade para desconto em restaurante
            Console.Write("Digite a idade: ");
            int idadeRestaurante = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(idadeRestaurante > 60 ? "Tem direito a desconto" : "Não tem direito a desconto");

            // Verificar velocidade do carro
            Console.Write("Digite a velocidade: ");
            int velocidade = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(velocidade > 100 ? "Multado" : "Dentro da velocidade permitida");

            // Número par ou ímpar (divisível por 3)
            Console.Write("Digite um número: ");
            int numParImpar = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(numParImpar % 3 == 0 ? "Divisível por 3" : "Não divisível por 3");

            // Verificação de número primo
            Console.Write("Digite um número: ");
            int numPrimo = Convert.ToInt32(Console.ReadLine());
            bool primo = true;
            for (int i = 2; i < numPrimo; i++)
            {
                if (numPrimo % i == 0)
                {
                    primo = false;
                    break;
                }
            }
            Console.WriteLine(primo ? "É primo" : "Não é primo");

            // Resultado de exame
            Console.Write("Digite a nota: ");
            double notaExame = Convert.ToDouble(Console.ReadLine());
            if (notaExame > 80) Console.WriteLine("Aprovado com louvor");
            else if (notaExame >= 60) Console.WriteLine("Aprovado");
            else Console.WriteLine("Reprovado");

            // Cálculo de área de retângulo
            Console.Write("Digite a base: ");
            double baseRet = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite a altura: ");
            double alturaRet = Convert.ToDouble(Console.ReadLine());
            if (baseRet > 10) Console.WriteLine($"Área: {baseRet * alturaRet}");
            else Console.WriteLine("Cálculo não pode ser realizado");

            // Definir tipo de triângulo
            Console.Write("Digite o lado 1: ");
            double lado1_1 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite o lado 2: ");
            double lado_2 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite o lado 3: ");
            double lado_3 = Convert.ToDouble(Console.ReadLine());
            if (lado1_1 == lado_2 && lado_2 == lado_3) Console.WriteLine("Equilátero");
            else if (lado1_1 == lado_2 || lado_2 == lado_3 || lado1_1 == lado_3) Console.WriteLine("Isósceles");
            else Console.WriteLine("Escaleno");

            // Estacionamento com desconto
            Console.Write("Digite as horas no estacionamento: ");
            int horasEst = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(horasEst > 3 ? $"Valor com desconto: {horasEst * 0.9}" : $"Valor integral: {horasEst}");

            // Calculando preço do ingresso no cinema
            Console.Write("O ingresso foi comprado antecipadamente? (s/n): ");
            char antecipado = Console.ReadLine()[0];
            Console.Write("Digite o preço do ingresso: ");
            double precoIngresso = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(antecipado == 's' ? $"Preço com desconto: {precoIngresso * 0.9}" : $"Preço normal: {precoIngresso}");

            // Cálculo de média ponderada
            Console.Write("Digite a nota 1: ");
            double notaP1 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite o peso 1: ");
            double peso1 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite a nota 2: ");
            double notaP2 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite o peso 2: ");
            double peso2 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite a nota 3: ");
            double notaP3 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite o peso 3: ");
            double peso3 = Convert.ToDouble(Console.ReadLine());
            double mediaPonderada = (notaP1 * peso1 + notaP2 * peso2 + notaP3 * peso3) / (peso1 + peso2 + peso3);
            Console.WriteLine(mediaPonderada >= 7 ? "Aprovado" : "Reprovado");

            // Tempo de viagem
            Console.Write("Digite a distância: ");
            double distancia = Convert.ToDouble(Console.ReadLine());
            Console.Write("Digite o tempo estimado: ");
            double tempo = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(tempo > distancia / 60 ? "Viagem demorada" : "Viagem no tempo esperado");

            // Renda superior à média
            Console.Write("Digite a renda mensal: ");
            double rendaMensal = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(rendaMensal > 2500 ? "Renda alta" : "Renda baixa");

            // Resultado de votação
            Console.Write("Digite os votos do candidato: ");
            int votos = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(votos > 50 ? "Eleito" : "Segundo turno");

            // Verificar faixa etária para seguro
            Console.Write("Digite a idade: ");
            int idadeSeguro = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(idadeSeguro >= 30 && idadeSeguro <= 40 ? "Seguro mais barato" : "Seguro mais caro");

            // Calculando preço com acréscimo
            Console.Write("Digite o valor da compra: ");
            double compraAcrescimo = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(compraAcrescimo > 200 ? $"Preço com acréscimo: {compraAcrescimo * 1.15}" : $"Preço normal: {compraAcrescimo}");

            // Resultado de temperatura
            Console.Write("Digite a temperatura: ");
            double tempResultado = Convert.ToDouble(Console.ReadLine());
            if (tempResultado < 0) Console.WriteLine("Frio extremo");
            else if (tempResultado < 15) Console.WriteLine("Frio");
            else if (tempResultado < 25) Console.WriteLine("Aconchegante");
            else Console.WriteLine("Calor");

            // Desconto para primeira compra
            Console.Write("É a primeira compra? (s/n): ");
            char primeiraCompra = Console.ReadLine()[0];
            Console.Write("Digite o valor da compra: ");
            double valorCompra_a = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(primeiraCompra == 's' ? $"Preço com desconto: {valorCompra * 0.8}" : $"Preço com desconto: {valorCompra * 0.9}");

            // Cálculo de tempo de viagem
            Console.Write("Digite o tempo estimado: ");
            double tempoViagem = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(tempoViagem > 5 ? "Recomenda-se parar para descansar" : "Viagem dentro do tempo esperado");

            // Determinar a categoria de filme
            Console.Write("Digite o valor do ingresso: ");
            double valorIngresso = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(valorIngresso > 20 ? "Filme premium" : "Filme comum");

            // Verificar cargo de funcionário
            Console.Write("Digite o cargo: ");
            string cargo = Console.ReadLine();
            Console.WriteLine(cargo == "Gerente" ? "Bônus de 15%" : "Bônus de 5%");

            // Verificação de saldo bancário
            Console.Write("Digite o saldo: ");
            double saldo = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(saldo < 0 ? "Conta no vermelho" : "Conta positiva");

            // Classificar idade em grupo etário
            Console.Write("Digite a idade: ");
            int idadeGrupo = Convert.ToInt32(Console.ReadLine());
            if (idadeGrupo <= 12) Console.WriteLine("Criança");
            else if (idadeGrupo <= 19) Console.WriteLine("Adolescente");
            else if (idadeGrupo <= 59) Console.WriteLine("Adulto");
            else Console.WriteLine("Idoso");

            // Calculando preço com imposto
            Console.Write("O produto é de eletrônicos? (s/n): ");
            char eletronico = Console.ReadLine()[0];
            Console.Write("Digite o valor do produto: ");
            double valorProdutoImposto = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(eletronico == 's' ? $"Preço com imposto: {valorProdutoImposto * 1.18}" : $"Preço com imposto: {valorProdutoImposto * 1.05}");

            // Verificar validade de produto
            Console.Write("Digite a data de validade (dd/mm/aaaa): ");
            DateTime validade = DateTime.Parse(Console.ReadLine());
            Console.WriteLine(validade < DateTime.Now ? "Vencido" : "Válido");

            // Verificação de pagamento em atraso
            Console.Write("Digite a data de vencimento (dd/mm/aaaa): ");
            DateTime vencimento = DateTime.Parse(Console.ReadLine());
            Console.Write("Digite a data de pagamento (dd/mm/aaaa): ");
            DateTime pagamento = DateTime.Parse(Console.ReadLine());
            Console.WriteLine(pagamento > vencimento ? $"Valor com multa: {valor * 1.05}" : "Pagamento no prazo");

            // Verificar categoria de aluno
            Console.Write("Digite a média: ");
            double mediaAluno = Convert.ToDouble(Console.ReadLine());
            if (mediaAluno >= 7) Console.WriteLine("Aprovado");
            else if (mediaAluno >= 5) Console.WriteLine("Recuperação");
            else Console.WriteLine("Reprovado");

            // Classificação de produtos de supermercado
            Console.Write("Digite o valor do produto: ");
            double valorProdutoSuper = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(valorProdutoSuper > 50 ? "Produtos caros" : "Produtos baratos");

            // Verificação de aceitação no concurso
            Console.Write("Digite a pontuação: ");
            int pontuacao = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(pontuacao > 70 ? "Aprovado" : "Reprovado");

            // Verificação de idade para entrar em uma festa
            Console.Write("Digite a idade: ");
            int idadeFesta = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(idadeFesta >= 18 ? "Pode entrar" : "Não pode entrar");

            // Calcular a área de um círculo
            Console.Write("Digite o raio: ");
            double raioCirculo = Convert.ToDouble(Console.ReadLine());
            if (raioCirculo > 10) Console.WriteLine($"Área: {Math.PI * raioCirculo * raioCirculo}");
            else Console.WriteLine("Área não pode ser calculada");

            // Verificar necessidade de idoso para acompanhante
            Console.Write("Digite a idade: ");
            int idadeIdoso = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(idadeIdoso > 75 ? "Tem direito a acompanhante" : "Não tem direito a acompanhante");

            // Quantidade de dias trabalhados
            Console.Write("Digite o número de dias trabalhados: ");
            int diasTrabalhados = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(diasTrabalhados > 20 ? "Tem direito ao prêmio" : "Não tem direito ao prêmio");

            // Verificar situação de dívida
            Console.Write("Digite o valor da dívida: ");
            double divida = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(divida > 1000 ? "Grande débito" : "Dívida pequena");

            // Idade para aluguel de carro
            Console.Write("Digite a idade: ");
            int idadeAluguel = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(idadeAluguel > 25 ? "Pode alugar o carro" : "Não pode alugar o carro");

            // Calcular média de temperatura diária
            double somaTemperaturas = 0;
            for (int i = 0; i < 7; i++)
            {
                Console.Write($"Digite a temperatura do dia {i + 1}: ");
                somaTemperaturas += Convert.ToDouble(Console.ReadLine());
            }
            double mediaTemperaturas = somaTemperaturas / 7;
            Console.WriteLine(mediaTemperaturas > 25 ? "Semana quente" : "Semana fria");

            // Definir se pode entrar na balada
            Console.Write("Digite a idade: ");
            int idadeBalada = Convert.ToInt32(Console.ReadLine());
            Console.Write("O nome está na lista? (s/n): ");
            char lista = Console.ReadLine()[0];
            Console.WriteLine(idadeBalada > 18 && lista == 's' ? "Pode entrar" : "Acesso negado");

            // Desconto no supermercado
            Console.Write("Digite o valor total da compra: ");
            double compraSuper = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(compraSuper > 150 ? $"Preço com desconto: {compraSuper * 0.9}" : "Sem desconto");

            // Classe de risco de seguro de vida
            Console.Write("Digite a idade: ");
            int idadeSeguroVida = Convert.ToInt32(Console.ReadLine());
            Console.Write("Tem histórico de doenças graves? (s/n): ");
            char historico = Console.ReadLine()[0];
            Console.WriteLine(idadeSeguroVida > 60 || historico == 's' ? "Classe de risco alto" : "Classe de risco baixa");

            // Resultado de curso
            Console.Write("Digite a nota final: ");
            double notaFinal = Convert.ToDouble(Console.ReadLine());
            if (notaFinal > 8) Console.WriteLine("Aprovado com mérito");
            else if (notaFinal >= 5) Console.WriteLine("Aprovado sem mérito");
            else Console.WriteLine("Reprovado");

            // Categoria de clima
            Console.Write("Digite a umidade do ar: ");
            double umidade = Convert.ToDouble(Console.ReadLine());
            if (umidade > 80) Console.WriteLine("Clima úmido");
            else if (umidade < 30) Console.WriteLine("Clima seco");
            else Console.WriteLine("Clima normal");

            // Cálculo de bônus de funcionário
            Console.Write("O funcionário atingiu a meta? (s/n): ");
            char meta = Console.ReadLine()[0];
            Console.Write("Digite o salário: ");
            double salarioBonus = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(meta == 's' ? $"Bônus: {salarioBonus * 0.2}" : "Sem bônus");





            }
        }
    }