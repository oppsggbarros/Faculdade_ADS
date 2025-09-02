import java.util.Scanner;

public class Exercicio27 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int maior = Integer.MIN_VALUE;
        int menor = Integer.MAX_VALUE;
        int numero;
        
        System.out.println("Digite números inteiros (negativo para encerrar):");
        
        do {
            System.out.print("Número: ");
            numero = scanner.nextInt();
            
            if (numero >= 0) {
                if (numero > maior) {
                    maior = numero;
                }
                if (numero < menor) {
                    menor = numero;
                }
            }
        } while (numero >= 0);
        
        if (maior != Integer.MIN_VALUE) {
            System.out.println("Maior número: " + maior);
            System.out.println("Menor número: " + menor);
        } else {
            System.out.println("Nenhum número válido foi informado.");
        }
        scanner.close();
    }
}