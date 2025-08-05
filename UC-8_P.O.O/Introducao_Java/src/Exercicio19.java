import java.util.Scanner;

public class Exercicio19 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite a nota da primeira prova: ");
        double nota1 = scanner.nextDouble();
        
        System.out.print("Digite a nota da segunda prova: ");
        double nota2 = scanner.nextDouble();
        
        System.out.print("Digite a nota da terceira prova: ");
        double nota3 = scanner.nextDouble();
        
        double media = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4;
        
        System.out.printf("Média do aluno: %.2f\n", media);
        
        if (media >= 60) {
            System.out.println("Aluno aprovado");
        } else {
            System.out.println("Aluno reprovado");
        }
        
        scanner.close();
    }
}