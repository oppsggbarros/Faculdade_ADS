import java.util.Scanner;

public class Exercicio9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o 1º número: ");
        int primeiro = scanner.nextInt();
        int maior = primeiro;
        int menor = primeiro;
        
        for (int i = 2; i <= 10; i++) {
            System.out.print("Digite o " + i + "º número: ");
            int numero = scanner.nextInt();
            
            if (numero > maior) {
                maior = numero;
            }
            if (numero < menor) {
                menor = numero;
            }
        }
        
        System.out.println("Menor valor: " + menor);
        System.out.println("Maior valor: " + maior);
        scanner.close();
    }
}