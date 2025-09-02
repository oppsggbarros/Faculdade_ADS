import java.util.Scanner;

public class Exercicio19 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalLidos = 0;
        int totalPares = 0;
        int numero;
        
        do {
            System.out.print("Digite um número (0 para terminar): ");
            numero = scanner.nextInt();
            
            if (numero != 0) {
                totalLidos++;
                if (numero % 2 == 0) {
                    totalPares++;
                }
            }
        } while (numero != 0);
        
        System.out.println("Total de números lidos: " + totalLidos);
        System.out.println("Total de números pares: " + totalPares);
        scanner.close();
    }
}