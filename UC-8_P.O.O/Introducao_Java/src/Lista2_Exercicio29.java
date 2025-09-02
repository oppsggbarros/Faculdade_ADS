import java.util.Scanner;

public class Exercicio29 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[5];
        int soma = 0;
        
        for (int i = 0; i < 5; i++) {
            System.out.print("Digite o " + (i + 1) + "º número: ");
            numeros[i] = scanner.nextInt();
            soma += numeros[i];
        }
        
        System.out.println("Soma: " + soma);
        System.out.println("Números digitados:");
        for (int i = 0; i < 5; i++) {
            System.out.println(numeros[i]);
        }
        scanner.close();
    }
}