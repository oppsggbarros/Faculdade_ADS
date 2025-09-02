import java.util.Scanner;

public class Exercicio16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o valor de n: ");
        int n = scanner.nextInt();
        
        int soma = 0;
        for (int i = 1; i <= n; i++) {
            soma += i;
        }
        
        System.out.println("Soma dos " + n + " primeiros números naturais: " + soma);
        scanner.close();
    }
}