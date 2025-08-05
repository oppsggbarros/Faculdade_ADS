import java.util.Scanner;

public class Exercicio20 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite a nota do trabalho de laboratório (0-10): ");
        double lab = scanner.nextDouble();
        
        System.out.print("Digite a nota da avaliação semestral (0-10): ");
        double semestral = scanner.nextDouble();
        
        System.out.print("Digite a nota do exame final (0-10): ");
        double exame = scanner.nextDouble();
        
        if (lab < 0 || lab > 10 || semestral < 0 || semestral > 10 || exame < 0 || exame > 10) {
            System.out.println("Notas inválidas. Todas devem estar entre 0 e 10");
        } else {
            double media = (lab * 2 + semestral * 3 + exame * 5) / 10;
            System.out.printf("Média final: %.2f\n", media);
            
            if (media >= 0 && media <= 2.9) {
                System.out.println("Aluno reprovado");
            } else if (media >= 3 && media <= 5.9) {
                System.out.println("Aluno em recuperação");
            } else {
                System.out.println("Aluno aprovado");
            }
        }
        
        scanner.close();
    }
}