import java.util.Scanner;

public class Exercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um número inteiro: ");
        int numero = scanner.nextInt();
        
        if (numero > 10) {
            System.out.println("É maior que 10");
        } else {
            System.out.println("É menor que 10");
        }
        
        scanner.close();
    }
}