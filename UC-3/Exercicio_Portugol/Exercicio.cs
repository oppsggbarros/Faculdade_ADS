using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Portugol_to_C_
{
    public class Test
    {
        static void Main(string[] args)
        {
            // 1. Soma de Dois Números
            Console.Write("Digite o primeiro número: ");
            double num1 = double.Parse(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            double num2 = double.Parse(Console.ReadLine());
            Console.WriteLine($"Soma: {num1 + num2}");

            // 2. Média de Notas
            Console.Write("Digite a primeira nota: ");
            double nota1 = double.Parse(Console.ReadLine());
            Console.Write("Digite a segunda nota: ");
            double nota2 = double.Parse(Console.ReadLine());
            Console.Write("Digite a terceira nota: ");
            double nota3 = double.Parse(Console.ReadLine());
            Console.WriteLine($"Média: {(nota1 + nota2 + nota3) / 3}");

            // 3. Conversão de Idade para Dias
            Console.Write("Digite a idade: ");
            int idade = int.Parse(Console.ReadLine());
            Console.WriteLine($"Dias vividos: {idade * 365}");

            // 4. Área de um Retângulo
            Console.Write("Digite a base: ");
            double baseRet = double.Parse(Console.ReadLine());
            Console.Write("Digite a altura: ");
            double alturaRet = double.Parse(Console.ReadLine());
            Console.WriteLine($"Área: {baseRet * alturaRet}");

            // 5. Conversão de Temperatura
            Console.Write("Digite a temperatura em Celsius: ");
            double celsius = double.Parse(Console.ReadLine());
            double fahrenheit = (celsius * 9 / 5) + 32;
            Console.WriteLine($"Temperatura em Fahrenheit: {fahrenheit}");

            // 6. Cálculo do IMC
            Console.Write("Digite o peso (kg): ");
            double peso = double.Parse(Console.ReadLine());
            Console.Write("Digite a altura (m): ");
            double altura = double.Parse(Console.ReadLine());
            double imc = peso / (altura * altura);
            Console.WriteLine($"IMC: {imc}");

            // 7. Desconto em uma Compra
            Console.Write("Digite o valor do produto: ");
            double valorProduto = double.Parse(Console.ReadLine());
            Console.Write("Digite o percentual de desconto: ");
            double desconto = double.Parse(Console.ReadLine());
            Console.WriteLine($"Valor com desconto: {valorProduto * (1 - desconto / 100)}");

            // 8. Conversão de Moeda
            Console.Write("Digite o valor em reais: ");
            double reais = double.Parse(Console.ReadLine());
            Console.WriteLine($"Valor em dólares: {reais / 5}");

            // 9. Combustível Necessário
            Console.Write("Digite a distância (km): ");
            double distancia = double.Parse(Console.ReadLine());
            Console.Write("Digite o consumo médio (km/L): ");
            double consumo = double.Parse(Console.ReadLine());
            Console.WriteLine($"Combustível necessário: {distancia / consumo} litros");

            // 10. Juros Simples
            Console.Write("Digite o capital: ");
            double capital = double.Parse(Console.ReadLine());
            Console.Write("Digite a taxa de juros (% ao mês): ");
            double taxa = double.Parse(Console.ReadLine());
            Console.Write("Digite o tempo (meses): ");
            int tempo = int.Parse(Console.ReadLine());
            double montante = capital + (capital * taxa / 100 * tempo);
            Console.WriteLine($"Montante: {montante}");

            // 11. Tabuada de um Número
            Console.Write("Digite um número: ");
            int numTabuada = int.Parse(Console.ReadLine());
            for (int i = 1; i <= 10; i++)
                Console.WriteLine($"{numTabuada} x {i} = {numTabuada * i}");

            // 12. Perímetro de um Círculo
            Console.Write("Digite o raio: ");
            double raio = double.Parse(Console.ReadLine());
            Console.WriteLine($"Perímetro: {2 * Math.PI * raio}");

            // 13. Troco de uma Compra
            Console.Write("Digite o valor total da compra: ");
            double totalCompra = double.Parse(Console.ReadLine());
            Console.Write("Digite o valor pago: ");
            double valorPago = double.Parse(Console.ReadLine());
            Console.WriteLine($"Troco: {valorPago - totalCompra}");

            // 14. Conversão de Horas para Minutos e Segundos
            Console.Write("Digite o valor em horas: ");
            double horas = double.Parse(Console.ReadLine());
            Console.WriteLine($"Minutos: {horas * 60}, Segundos: {horas * 3600}");

            // 15. Salário com Aumento
            Console.Write("Digite o salário atual: ");
            double salario = double.Parse(Console.ReadLine());
            Console.Write("Digite o percentual de aumento: ");
            double aumento = double.Parse(Console.ReadLine());
            Console.WriteLine($"Novo salário: {salario * (1 + aumento / 100)}");

            // 16. Diferença entre Dois Números
            Console.Write("Digite o primeiro número: ");
            double numA = double.Parse(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            double numB = double.Parse(Console.ReadLine());
            Console.WriteLine($"Diferença absoluta: {Math.Abs(numA - numB)}");

            // 17. Divisão e Resto
            Console.Write("Digite o primeiro número: ");
            int numDiv1 = int.Parse(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            int numDiv2 = int.Parse(Console.ReadLine());
            Console.WriteLine($"Divisão inteira: {numDiv1 / numDiv2}, Resto: {numDiv1 % numDiv2}");

            // 18. Preço Final com Parcelamento
            Console.Write("Digite o valor do produto: ");
            double valorProdutoParcela = double.Parse(Console.ReadLine());
            Console.Write("Digite a quantidade de parcelas: ");
            int parcelas = int.Parse(Console.ReadLine());
            Console.WriteLine($"Valor de cada parcela: {valorProdutoParcela / parcelas}");

            // 19. Média Ponderada
            Console.Write("Digite a primeira nota: ");
            double notaP1 = double.Parse(Console.ReadLine());
            Console.Write("Digite o peso da primeira nota: ");
            double pesoP1 = double.Parse(Console.ReadLine());
            Console.Write("Digite a segunda nota: ");
            double notaP2 = double.Parse(Console.ReadLine());
            Console.Write("Digite o peso da segunda nota: ");
            double pesoP2 = double.Parse(Console.ReadLine());
            Console.Write("Digite a terceira nota: ");
            double notaP3 = double.Parse(Console.ReadLine());
            Console.Write("Digite o peso da terceira nota: ");
            double pesoP3 = double.Parse(Console.ReadLine());
            double mediaPonderada = (notaP1 * pesoP1 + notaP2 * pesoP2 + notaP3 * pesoP3) / (pesoP1 + pesoP2 + pesoP3);
            Console.WriteLine($"Média ponderada: {mediaPonderada}");

            // 20. Tempo de Viagem
            Console.Write("Digite a distância (km): ");
            double distanciaViagem = double.Parse(Console.ReadLine());
            Console.Write("Digite a velocidade média (km/h): ");
            double velocidade = double.Parse(Console.ReadLine());
            Console.WriteLine($"Tempo estimado: {distanciaViagem / velocidade} horas");

            // 21. Conversão de Segundos para Horas, Minutos e Segundos
            Console.Write("Digite o valor em segundos: ");
            int segundos = int.Parse(Console.ReadLine());
            int horasConv = segundos / 3600;
            int minutosConv = (segundos % 3600) / 60;
            int segundosConv = segundos % 60;
            Console.WriteLine($"{horasConv}h {minutosConv}m {segundosConv}s");

            // 22. Cálculo do Volume de um Cilindro
            Console.Write("Digite o raio: ");
            double raioCilindro = double.Parse(Console.ReadLine());
            Console.Write("Digite a altura: ");
            double alturaCilindro = double.Parse(Console.ReadLine());
            Console.WriteLine($"Volume: {Math.PI * raioCilindro * raioCilindro * alturaCilindro}");

            // 23. Troca de Valores entre Variáveis
            Console.Write("Digite o primeiro número: ");
            int numTroca1 = int.Parse(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            int numTroca2 = int.Parse(Console.ReadLine());
            Console.WriteLine($"Antes da troca: {numTroca1}, {numTroca2}");
            int temp = numTroca1;
            numTroca1 = numTroca2;
            numTroca2 = temp;
            Console.WriteLine($"Depois da troca: {numTroca1}, {numTroca2}");

            // 24. Cálculo do Lucro de um Produto
            Console.Write("Digite o preço de custo: ");
            double custo = double.Parse(Console.ReadLine());
            Console.Write("Digite o preço de venda: ");
            double venda = double.Parse(Console.ReadLine());
            double lucroPercentual = ((venda - custo) / custo) * 100;
            Console.WriteLine($"Lucro percentual: {lucroPercentual}%");

            // 25. Cálculo do Novo Preço com Inflação
            Console.Write("Digite o preço do produto: ");
            double precoProduto = double.Parse(Console.ReadLine());
            Console.Write("Digite a taxa de inflação mensal (%): ");
            double inflacao = double.Parse(Console.ReadLine());
            Console.Write("Digite o número de meses: ");
            int meses = int.Parse(Console.ReadLine());
            double novoPreco = precoProduto * Math.Pow(1 + inflacao / 100, meses);
            Console.WriteLine($"Novo preço: {novoPreco}");

            // 26. Conversão de KM/h para M/s
            Console.Write("Digite a velocidade em km/h: ");
            double velocidadeKmh = double.Parse(Console.ReadLine());
            Console.WriteLine($"Velocidade em m/s: {velocidadeKmh / 3.6}");

            // 27. Cálculo de Hipotenusa (Teorema de Pitágoras)
            Console.Write("Digite o valor do primeiro cateto: ");
            double cateto1 = double.Parse(Console.ReadLine());
            Console.Write("Digite o valor do segundo cateto: ");
            double cateto2 = double.Parse(Console.ReadLine());
            double hipotenusa = Math.Sqrt(cateto1 * cateto1 + cateto2 * cateto2);
            Console.WriteLine($"Hipotenusa: {hipotenusa}");

            // 28. Quantidade de Latas de Tinta
            Console.Write("Digite a área a ser pintada (m²): ");
            double areaPintada = double.Parse(Console.ReadLine());
            Console.Write("Digite o rendimento da tinta (m²/L): ");
            double rendimentoTinta = double.Parse(Console.ReadLine());
            Console.WriteLine($"Latas necessárias: {Math.Ceiling(areaPintada / rendimentoTinta)}");

            // 29. Contagem de Cédulas para um Saque
            Console.Write("Digite o valor do saque: ");
            int saque = int.Parse(Console.ReadLine());
            int[] cedulas = { 100, 50, 20, 10, 5, 2 };
            foreach (int cedula in cedulas)
            {
                int quantidade = saque / cedula;
                if (quantidade > 0)
                {
                    Console.WriteLine($"{quantidade} cédula(s) de R${cedula}");
                    saque %= cedula;
                }
            }

            // 30. Cálculo do Perímetro e Área de um Quadrado
            Console.Write("Digite o lado do quadrado: ");
            double ladoQuadrado = double.Parse(Console.ReadLine());
            Console.WriteLine($"Perímetro: {4 * ladoQuadrado}, Área: {ladoQuadrado * ladoQuadrado}");

            // 31. Cálculo do Peso Ideal
            Console.Write("Digite a altura (m): ");
            double alturaPesoIdeal = double.Parse(Console.ReadLine());
            double pesoIdeal = (72.7 * alturaPesoIdeal) - 58;
            Console.WriteLine($"Peso ideal: {pesoIdeal} kg");

            // 32. Valor Total de uma Conta de Restaurante
            Console.Write("Digite o valor da conta: ");
            double conta = double.Parse(Console.ReadLine());
            Console.WriteLine($"Valor total com serviço: {conta * 1.1}");

            // 33. Tempo de Download de um Arquivo
            Console.Write("Digite o tamanho do arquivo (MB): ");
            double tamanhoArquivo = double.Parse(Console.ReadLine());
            Console.Write("Digite a velocidade da internet (Mbps): ");
            double velocidadeInternet = double.Parse(Console.ReadLine());
            Console.WriteLine($"Tempo estimado de download: {tamanhoArquivo / velocidadeInternet} segundos");

            // 34. Cálculo da Distância entre Dois Pontos
            Console.Write("Digite x1: ");
            double x1 = double.Parse(Console.ReadLine());
            Console.Write("Digite y1: ");
            double y1 = double.Parse(Console.ReadLine());
            Console.Write("Digite x2: ");
            double x2 = double.Parse(Console.ReadLine());
            Console.Write("Digite y2: ");
            double y2 = double.Parse(Console.ReadLine());
            double distanciaPontos = Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2));
            Console.WriteLine($"Distância: {distanciaPontos}");

            // 35. Conversão de Litros para Mililitros
            Console.Write("Digite o valor em litros: ");
            double litros = double.Parse(Console.ReadLine());
            Console.WriteLine($"Mililitros: {litros * 1000}");

            // 36. Número de Azulejos Necessários para um Piso
            Console.Write("Digite a área do piso (m²): ");
            double areaPiso = double.Parse(Console.ReadLine());
            Console.Write("Digite o tamanho de cada azulejo (m²): ");
            double tamanhoAzulejo = double.Parse(Console.ReadLine());
            Console.WriteLine($"Quantidade de azulejos: {Math.Ceiling(areaPiso / tamanhoAzulejo)}");

            // 37. Cálculo de Preço Final com Imposto
            Console.Write("Digite o valor do produto: ");
            double valorProdutoImposto = double.Parse(Console.ReadLine());
            Console.Write("Digite a taxa de imposto (%): ");
            double imposto = double.Parse(Console.ReadLine());
            Console.WriteLine($"Valor final: {valorProdutoImposto * (1 + imposto / 100)}");

            // 38. Comparação entre Dois Números
            Console.Write("Digite o primeiro número: ");
            double numComp1 = double.Parse(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            double numComp2 = double.Parse(Console.ReadLine());
            if (numComp1 > numComp2) Console.WriteLine("O primeiro número é maior");
            else if (numComp2 > numComp1) Console.WriteLine("O segundo número é maior");
            else Console.WriteLine("Os números são iguais");

            // 39. Transformação de String para Maiúsculas
            Console.Write("Digite um nome: ");
            string nome = Console.ReadLine();
            Console.WriteLine($"Nome em maiúsculas: {nome.ToUpper()}");

            // 40. Soma dos Algarismos de um Número
            Console.Write("Digite um número de dois dígitos: ");
            int numDigitos = int.Parse(Console.ReadLine());
            int somaDigitos = (numDigitos / 10) + (numDigitos % 10);
            Console.WriteLine($"Soma dos algarismos: {somaDigitos}");

            // 41. Multiplicação de Dois Números sem Usar *
            Console.Write("Digite o primeiro número: ");
            int numMult1 = int.Parse(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            int numMult2 = int.Parse(Console.ReadLine());
            int resultado = 0;
            for (int i = 0; i < numMult2; i++) resultado += numMult1;
            Console.WriteLine($"Resultado: {resultado}");

            // 42. Reajuste de Mensalidade Escolar
            Console.Write("Digite o valor da mensalidade: ");
            double mensalidade = double.Parse(Console.ReadLine());
            Console.Write("Digite o percentual de aumento: ");
            double aumentoMensalidade = double.Parse(Console.ReadLine());
            Console.WriteLine($"Novo valor: {mensalidade * (1 + aumentoMensalidade / 100)}");

            // 43. Valor Final de um Investimento com Juros Compostos
            Console.Write("Digite o capital: ");
            double capitalJuros = double.Parse(Console.ReadLine());
            Console.Write("Digite a taxa de juros (% ao mês): ");
            double taxaJuros = double.Parse(Console.ReadLine());
            Console.Write("Digite o tempo (meses): ");
            int tempoJuros = int.Parse(Console.ReadLine());
            double montanteJuros = capitalJuros * Math.Pow(1 + taxaJuros / 100, tempoJuros);
            Console.WriteLine($"Montante final: {montanteJuros}");

            // 44. Conversão de Massa (Kg para Gramas e Toneladas)
            Console.Write("Digite o valor em kg: ");
            double kg = double.Parse(Console.ReadLine());
            Console.WriteLine($"Gramas: {kg * 1000}, Toneladas: {kg / 1000}");

            // 45. Conversão de Tempo (Dias para Horas, Minutos e Segundos)
            Console.Write("Digite o valor em dias: ");
            int dias = int.Parse(Console.ReadLine());
            Console.WriteLine($"Horas: {dias * 24}, Minutos: {dias * 1440}, Segundos: {dias * 86400}");

            // 46. Soma dos Números Ímpares de um Intervalo
            Console.Write("Digite o primeiro número: ");
            int numInicio = int.Parse(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            int numFim = int.Parse(Console.ReadLine());
            int somaImpares = 0;
            for (int i = numInicio; i <= numFim; i++)
                if (i % 2 != 0) somaImpares += i;
            Console.WriteLine($"Soma dos ímpares: {somaImpares}");

            // 47. Conversão de Notas de Alunos (0-10 para 0-100)
            Console.Write("Digite a nota (0-10): ");
            double notaEscala = double.Parse(Console.ReadLine());
            Console.WriteLine($"Nota em 0-100: {notaEscala * 10}");

            // 48. Cálculo de Quilowatt-hora (Conta de Energia)
            Console.Write("Digite o consumo de energia (kWh): ");
            double consumoEnergia = double.Parse(Console.ReadLine());
            Console.Write("Digite o preço por kWh: ");
            double precoKwh = double.Parse(Console.ReadLine());
            Console.WriteLine($"Valor da conta: {consumoEnergia * precoKwh}");

            // 49. Conversão de Milhas para Quilômetros
            Console.Write("Digite a distância em milhas: ");
            double milhas = double.Parse(Console.ReadLine());
            Console.WriteLine($"Distância em km: {milhas * 1.609}");

            // 50. Cálculo do Consumo de Água
            Console.Write("Digite o consumo médio de água (litros/dia): ");
            double consumoAgua = double.Parse(Console.ReadLine());
            Console.WriteLine($"Consumo mensal: {consumoAgua * 30} litros, Consumo anual: {consumoAgua * 365} litros");






        }
    }
}