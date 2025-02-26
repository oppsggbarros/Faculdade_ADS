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
            int fatorial = 1;
            for (int n = 1; n <= 10; n++)
            {
                fatorial *= n;
                Console.WriteLine(n + " fatorial= " + fatorial);
            }
        }
    }
}