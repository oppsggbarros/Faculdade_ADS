import java.util.Scanner;

public class Exercicio43 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Nome do atleta: ");
        String nome = scanner.nextLine();
        
        double[] notas = new double[7];
        double melhorNota = Double.MIN_VALUE;
        double piorNota = Double.MAX_VALUE;
        double soma = 0;
        
        for (int i = 0; i < 7; i++) {
            System.out.print("Nota " + (i + 1) + ": ");
            notas[i] = scanner.nextDouble();
            
            if (notas[i] > melhorNota) {
                melhorNota = notas[i];
            }
            if (notas[i] < piorNota) {
                piorNota = notas[i];
            }
            soma += notas[i];
        }
        
        double media = (soma - melhorNota - piorNota) / 5;
        
        System.out.println("\n=== RESULTADO FINAL ===");
        System.out.println("Atleta: " + nome);
        System.out.println("Melhor nota: " + melhorNota);
        System.out.println("Pior nota: " + piorNota);
        System.out.printf("Média: %.2f\n", media);
        scanner.close();
    }
}