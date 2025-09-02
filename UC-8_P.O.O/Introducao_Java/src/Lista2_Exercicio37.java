import java.util.Scanner;

public class Exercicio37 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.print("Digite R1 (0 para sair): ");
            double r1 = scanner.nextDouble();
            if (r1 == 0) break;
            
            System.out.print("Digite R2 (0 para sair): ");
            double r2 = scanner.nextDouble();
            if (r2 == 0) break;
            
            if (r1 == 0 || r2 == 0) {
                System.out.println("Resistência não pode ser zero!");
                continue;
            }
            
            double resistenciaEquivalente = (r1 * r2) / (r1 + r2);
            System.out.printf("Resistência equivalente: %.2f ohms\n\n", resistenciaEquivalente);
        }
        scanner.close();
    }
}