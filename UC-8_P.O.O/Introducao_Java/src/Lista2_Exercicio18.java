import java.util.Scanner;

public class Exercicio18 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número entre 100 e 9999: ");
        int numero = scanner.nextInt();
        
        if (numero >= 100 && numero <= 9999) {
            String numeroStr = String.valueOf(numero);
            System.out.println("Algarismos:");
            for (int i = 0; i < numeroStr.length(); i++) {
                System.out.println(numeroStr.charAt(i));
            }
        } else {
            System.out.println("Número fora do intervalo permitido!");
        }
        scanner.close();
    }
}