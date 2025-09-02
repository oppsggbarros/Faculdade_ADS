import java.util.Scanner;

public class Exercicio10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o valor de N: ");
        int n = scanner.nextInt();
        
        int count = 0;
        int numero = 1;
        
        while (count < n) {
            if (numero % 2 != 0) {
                System.out.println(numero);
                count++;
            }
            numero++;
        }
        scanner.close();
    }
}