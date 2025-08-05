import java.util.Scanner;

public class Exercicio26 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o primeiro lado do triângulo: ");
        double a = scanner.nextDouble();
        
        System.out.print("Digite o segundo lado do triângulo: ");
        double b = scanner.nextDouble();
        
        System.out.print("Digite o terceiro lado do triângulo: ");
        double c = scanner.nextDouble();
        
        if (a < b + c && b < a + c && c < a + b) {
            if (a == b && b == c) {
                System.out.println("Triângulo equilátero");
            } else if (a == b || a == c || b == c) {
                System.out.println("Triângulo isósceles");
            } else {
                System.out.println("Triângulo escaleno");
            }
        } else {
            System.out.println("Os valores não formam um triângulo");
        }
        
        scanner.close();
    }
}