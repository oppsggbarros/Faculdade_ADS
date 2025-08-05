import java.util.Scanner;

public class Exercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o primeiro número inteiro: ");
        int num1 = scanner.nextInt();
        
        System.out.print("Digite o segundo número inteiro: ");
        int num2 = scanner.nextInt();
        
        System.out.print("Digite um número real: ");
        double num3 = scanner.nextDouble();
        
        double resultado1 = num1 * (num2 / 2.0);
        double resultado2 = (3 * num1) + num3;
        double resultado3 = Math.pow(num3, 3);
        
        System.out.println("O produto do primeiro com a metade do segundo: " + resultado1);
        System.out.println("A soma do triplo do primeiro com o terceiro: " + resultado2);
        System.out.println("O terceiro número ao cubo: " + resultado3);
        
        scanner.close();
    }
}