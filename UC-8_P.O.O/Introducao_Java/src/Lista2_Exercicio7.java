import java.util.Scanner;

public class Exercicio7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int soma = 0;
        
        for (int i = 1; i <= 10; i++) {
            System.out.print("Digite o " + i + "º inteiro: ");
            int numero = scanner.nextInt();
            soma += numero;
        }
        
        double media = soma / 10.0;
        System.out.println("Média: " + media);
        scanner.close();
    }
}