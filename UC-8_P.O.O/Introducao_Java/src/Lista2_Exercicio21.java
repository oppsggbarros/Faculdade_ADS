import java.util.Scanner;

public class Exercicio21 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double soma = 0;
        int count = 0;
        double nota;
        
        System.out.println("Digite as notas (0-10). Qualquer valor fora deste intervalo encerra:");
        
        while (true) {
            System.out.print("Nota " + (count + 1) + ": ");
            nota = scanner.nextDouble();
            
            if (nota < 0 || nota > 10) {
                break;
            }
            
            soma += nota;
            count++;
        }
        
        if (count > 0) {
            double media = soma / count;
            System.out.println("Média: " + media);
        } else {
            System.out.println("Nenhuma nota válida foi informada.");
        }
        scanner.close();
    }
}