import java.util.Scanner;

public class Exercicio38 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.print("Digite um número (<= 0 para sair): ");
            double numero = scanner.nextDouble();
            
            if (numero <= 0) break;
            
            double quadrado = numero * numero;
            double cubo = numero * numero * numero;
            double raiz = Math.sqrt(numero);
            
            System.out.printf("Quadrado: %.2f\n", quadrado);
            System.out.printf("Cubo: %.2f\n", cubo);
            System.out.printf("Raiz quadrada: %.2f\n\n", raiz);
        }
        scanner.close();
    }
}