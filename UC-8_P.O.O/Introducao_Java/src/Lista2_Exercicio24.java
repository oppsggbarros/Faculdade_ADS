import java.util.Scanner;

public class Exercicio24 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int soma = 0;
        int count = 0;
        int idade;
        
        System.out.println("Digite as idades (0 para encerrar):");
        
        do {
            System.out.print("Idade: ");
            idade = scanner.nextInt();
            
            if (idade != 0) {
                soma += idade;
                count++;
            }
        } while (idade != 0);
        
        if (count > 0) {
            double media = (double) soma / count;
            System.out.println("Média de idade: " + media);
        } else {
            System.out.println("Nenhuma idade foi informada.");
        }
        scanner.close();
    }
}