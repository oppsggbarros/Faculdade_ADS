import java.util.Scanner;

public class Exercicio12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o primeiro número inteiro: ");
        int num1 = scanner.nextInt();
        
        System.out.print("Digite o segundo número inteiro: ");
        int num2 = scanner.nextInt();
        
        int maior = Math.max(num1, num2);
        int diferenca = Math.abs(num1 - num2);
        
        System.out.println("O maior número é: " + maior);
        System.out.println("A diferença entre eles é: " + diferenca);
        
        scanner.close();
    }
}