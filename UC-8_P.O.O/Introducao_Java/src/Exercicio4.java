import java.util.Scanner;

public class Exercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o primeiro número: ");
        double num1 = scanner.nextDouble();
        
        System.out.print("Digite o segundo número: ");
        double num2 = scanner.nextDouble();
        
        System.out.print("Digite o terceiro número: ");
        double num3 = scanner.nextDouble();
        
        if (num1 < num2 && num2 < num3) {
            System.out.println("Os números estão em ordem crescente");
        } else {
            System.out.println("Os números NÃO estão em ordem crescente");
        }
        
        scanner.close();
    }
}