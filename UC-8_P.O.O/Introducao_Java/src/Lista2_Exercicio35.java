import java.util.Scanner;

public class Exercicio35 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número não negativo n: ");
        int n = scanner.nextInt();
        
        int soma = 0;
        int count = 0;
        int numero = 2;
        
        while (count < n) {
            if (isPrimo(numero)) {
                soma += numero;
                count++;
            }
            numero++;
        }
        
        System.out.println("Soma dos " + n + " primeiros números primos: " + soma);
        scanner.close();
    }
    
    private static boolean isPrimo(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}