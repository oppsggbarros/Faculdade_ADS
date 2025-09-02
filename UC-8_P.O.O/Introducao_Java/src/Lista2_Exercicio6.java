import java.util.Scanner;

public class Exercicio6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int soma = 0;
        
        for (int i = 1; i <= 10; i++) {
            System.out.print("Digite o " + i + "º valor: ");
            int valor = scanner.nextInt();
            soma += valor;
        }
        
        System.out.println("Soma total: " + soma);
        scanner.close();
    }
}