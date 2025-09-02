import java.util.Scanner;

public class Exercicio17 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Quantos números deseja ler? ");
        int quantidade = scanner.nextInt();
        
        int maior = Integer.MIN_VALUE;
        
        for (int i = 1; i <= quantidade; i++) {
            System.out.print("Digite o " + i + "º número: ");
            int numero = scanner.nextInt();
            
            if (numero > maior) {
                maior = numero;
            }
        }
        
        System.out.println("O maior número é: " + maior);
        scanner.close();
    }
}