import java.util.Scanner;

public class Exercicio9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o primeiro número: ");
        double num1 = scanner.nextDouble();
        
        System.out.print("Digite o segundo número: ");
        double num2 = scanner.nextDouble();
        
        // Invertendo os valores
        double temp = num1;
        num1 = num2;
        num2 = temp;
        
        System.out.println("Valores invertidos:");
        System.out.println("Primeiro número: " + num1);
        System.out.println("Segundo número: " + num2);
        
        scanner.close();
    }
}