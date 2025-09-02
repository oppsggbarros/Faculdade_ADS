import java.util.Scanner;

public class Exercicio22 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número inteiro: ");
        int numero = scanner.nextInt();
        
        int soma = 0;
        System.out.print("Divisores: ");
        for (int i = 1; i < numero; i++) {
            if (numero % i == 0) {
                soma += i;
                System.out.print(i + " ");
            }
        }
        
        System.out.println("\nSoma dos divisores próprios: " + soma);
        scanner.close();
    }
}