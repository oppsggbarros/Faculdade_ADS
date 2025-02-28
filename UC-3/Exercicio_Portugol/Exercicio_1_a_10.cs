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
            // System.Console.WriteLine("Exercicio 1");
            // int a, b;
            // Console.WriteLine("Primeiro número: ");
            // a = Convert.ToInt32(Console.ReadLine());
            // Console.WriteLine("Segundo número: ");
            // b = Convert.ToInt32(Console.ReadLine());
            // Console.WriteLine($"Soma: " + (a + b));

            // System.Console.WriteLine("Exercicio 2");
            // int a, b, c;
            // float media;
            // Console.WriteLine("Primeiro número: ");
            // a = Convert.ToInt32(Console.ReadLine());
            // Console.WriteLine("Segundo número: ");
            // b = Convert.ToInt32(Console.ReadLine());
            // Console.WriteLine("Terceiro número: ");
            // c = Convert.ToInt32(Console.ReadLine());
            // media = (a + b + c) / 3;
            // Console.WriteLine($"Média: " + media);
            
            // System.Console.WriteLine("Exercicio 3");
            // int idade;
            // Console.WriteLine("Idade: ");
            // idade = Convert.ToInt32(Console.ReadLine());
            // System.Console.WriteLine("Você viveu por  aproximadamente" + (idade*365) + " Dias");

            System.Console.WriteLine("Exercicio 4");
            int a, b;
            Console.WriteLine("Base: ");
            a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Altura: ");
            b = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine($"Área: " + (a * b) / 2);
        }
    }
}