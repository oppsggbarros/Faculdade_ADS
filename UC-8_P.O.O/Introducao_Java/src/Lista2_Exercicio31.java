import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exercicio31 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Integer> numeros = new ArrayList<>();
        List<Integer> pares = new ArrayList<>();
        List<Integer> impares = new ArrayList<>();
        
        System.out.println("Digite 20 números inteiros:");
        for (int i = 0; i < 20; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            int numero = scanner.nextInt();
            numeros.add(numero);
            
            if (numero % 2 == 0) {
                pares.add(numero);
            } else {
                impares.add(numero);
            }
        }
        
        System.out.println("\nTodos os números: " + numeros);
        System.out.println("Números pares: " + pares);
        System.out.println("Números ímpares: " + impares);
        scanner.close();
    }
}