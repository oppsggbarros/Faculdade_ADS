import java.util.Scanner;

public class Exercicio14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número inteiro positivo par N: ");
        int n = scanner.nextInt();
        
        if (n % 2 == 0) {
            for (int i = n; i >= 0; i -= 2) {
                System.out.println(i);
            }
        } else {
            System.out.println("O número digitado não é par!");
        }
        scanner.close();
    }
}