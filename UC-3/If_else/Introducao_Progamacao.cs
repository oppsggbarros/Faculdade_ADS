using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace If_else
{
    public class Introducao_Progamacao
    {
        static void Main(string[] args)
        {
            // Exercicio 1
            int num1;
            int num2;
            System.Console.WriteLine("Digite o primeiro numero");
            num1 = Convert.ToInt32(Console.ReadLine());
            System.Console.WriteLine("Digite o segundo numero");
            num2 = Convert.ToInt32(Console.ReadLine());

            if (num1 > num2)
            {
                Console.WriteLine("O primeiro número é maior");
            }
            else if (num2 > num1)
            {
                Console.WriteLine("O segundo número é maior");
            }
            else
            {
                System.Console.WriteLine("Digite um numero valido");
            }

            // Exercicio 2
            int data;
            System.Console.WriteLine("Informe o ano de nascimento");
            data = Convert.ToInt32(Console.ReadLine());
            if (data < 2025 - 16)
            {
                Console.WriteLine("Voce pode votar");
            }
            else
            {
                Console.WriteLine("Voce não pode votar");
            }

            // Exercicio 3
            int senha = 1234;
            int senha_digitada;
            System.Console.WriteLine("Digite a senha");
            senha_digitada = Convert.ToInt32(Console.ReadLine());
            if (senha == senha_digitada)
            {
                Console.WriteLine("Acesso permitido");
            }
            else
            {
                Console.WriteLine("Acesso negado");
            }

            // Exercicio 4
            double preco_maca = 0.30;
            int quantidade;
            double total;
            System.Console.WriteLine("Quantas macas você deseja comprar?");
            quantidade = Convert.ToInt32(Console.ReadLine());
            if (quantidade >= 12)
            {
                total = (preco_maca - 0.05)*quantidade;
                Console.WriteLine("O valor total é: " + total);
            }
            else
            {
                total = preco_maca * quantidade;
            }

            // Exercicio 5
            int[] numeros = new int[3];
            System.Console.WriteLine("Digite 3 numeros");
            for (int i = 0; i < 3; i++)
            {
                numeros[i] = Convert.ToInt32(Console.ReadLine());

            }
            Array.Sort(numeros);
            Console.WriteLine("Os numeros em ordem crescente são: " + numeros[0] + " " + numeros[1] + " " + numeros[2]);

            // Exercicio 6
            char sexo;
            double altura;
            double result;

            System.Console.WriteLine("Digite o sexo (M/F)");
            sexo = Convert.ToChar(Console.ReadLine());
            System.Console.WriteLine("Digite a altura");
            altura = Convert.ToDouble(Console.ReadLine());
            if (sexo == 'M')
            {
                result = (72.7 * altura) - 58;
                System.Console.WriteLine("Seu peso ideal é: " + result);
            }
            else if (sexo == 'F')
            {
                result = (62.1 * altura) - 44.7;
                System.Console.WriteLine("Seu peso ideal é: " + result);
            }
            else
            {
                System.Console.WriteLine("Sexo invalido");
            }

            // Exercicio 9 
            int numero1, numero2, numero3;
            System.Console.WriteLine("Digite 3 numeros");
            numero1 = Convert.ToInt32(Console.ReadLine());
            numero2 = Convert.ToInt32(Console.ReadLine());
            numero3 = Convert.ToInt32(Console.ReadLine());
            if (numero1 > numero2 && numero1 > numero3)
            {
                System.Console.WriteLine("O maior numero é o primeiro numero");
            }
            else if (numero2 > numero1 && numero2 > numero3)
            {
                System.Console.WriteLine("O maior numero é o segundo numero");
            }
            else
            {
                System.Console.WriteLine("O maior numero é o terceiro numero");
            }

            // Exercicio 10
            int lado1, lado2, lado3;
            System.Console.WriteLine("Digite 3 lados de um triangulo");
            lado1 = Convert.ToInt32(Console.ReadLine());
            lado2 = Convert.ToInt32(Console.ReadLine());
            lado3 = Convert.ToInt32(Console.ReadLine());
            if (lado1 == lado2 && lado1 == lado3)
            {
                System.Console.WriteLine("O triangulo é equilatero");
            }
            else if (lado1 == lado2 || lado1 == lado3 || lado2 == lado3)
            {
                System.Console.WriteLine("O triangulo é isosceles");
            }
            else
            {
                System.Console.WriteLine("O triangulo é escaleno");
            }
            // Exercicio 11
            int angulo1;
            int angulo2;
            int angulo3;
            System.Console.WriteLine("Digite 3 angulos de um triangulo");
            angulo1 = Convert.ToInt32(Console.ReadLine());
            angulo2 = Convert.ToInt32(Console.ReadLine());
            angulo3 = Convert.ToInt32(Console.ReadLine());
            if (angulo1 == 90 || angulo2 == 90 || angulo3 == 90)
            {
                System.Console.WriteLine("O triangulo é retangulo");
            }
            else if (angulo1 > 90 || angulo2 > 90 || angulo3 > 90)
            {
                System.Console.WriteLine("O triangulo é obtusangulo");
            }
            else
            {
                System.Console.WriteLine("O triangulo é acutangulo");
            }





            
        }
    }
}