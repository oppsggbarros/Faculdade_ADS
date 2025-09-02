import java.util.Scanner;

public class Exercicio8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int soma = 0;
        int count = 0;
        
        while (count < 10) {
            System.out.print("Digite um número positivo: ");
            int numero = scanner.nextInt();
            
            if (numero > 0) {
                soma += numero;
                count++;
            } else {
                System.out.println("Número ignorado (não positivo)");
            }
        }
        
        double media = soma / 10.0;
        System.out.println("Média: " + media);
        scanner.close();
    }
}