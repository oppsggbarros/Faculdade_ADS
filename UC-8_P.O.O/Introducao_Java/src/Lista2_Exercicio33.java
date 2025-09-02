import java.util.Scanner;

public class Exercicio33 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] medias = new double[10];
        int aprovados = 0;
        
        for (int i = 0; i < 10; i++) {
            System.out.println("Aluno " + (i + 1) + ":");
            double somaNotas = 0;
            
            for (int j = 0; j < 4; j++) {
                System.out.print("Nota " + (j + 1) + ": ");
                somaNotas += scanner.nextDouble();
            }
            
            medias[i] = somaNotas / 4;
            if (medias[i] >= 7.0) {
                aprovados++;
            }
        }
        
        System.out.println("Número de alunos com média >= 7.0: " + aprovados);
        scanner.close();
    }
}