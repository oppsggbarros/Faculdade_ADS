import java.util.Scanner;

public class Exercicio14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite a primeira nota: ");
        double nota1 = scanner.nextDouble();
        
        System.out.print("Digite a segunda nota: ");
        double nota2 = scanner.nextDouble();
        
        if (nota1 < 0 || nota1 > 10 || nota2 < 0 || nota2 > 10) {
            System.out.println("Nota inválida. As notas devem estar entre 0.0 e 10.0");
        } else {
            double media = (nota1 + nota2) / 2;
            System.out.printf("A média das notas é: %.2f\n", media);
        }
        
        scanner.close();
    }
}