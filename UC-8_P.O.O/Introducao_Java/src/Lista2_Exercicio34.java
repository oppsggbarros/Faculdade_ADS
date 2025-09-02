import java.util.Scanner;

public class Exercicio34 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número maior que 1: ");
        int numero = scanner.nextInt();
        
        if (numero <= 1) {
            System.out.println("Número deve ser maior que 1!");
        } else {
            boolean primo = true;
            
            for (int i = 2; i <= Math.sqrt(numero); i++) {
                if (numero % i == 0) {
                    primo = false;
                    break;
                }
            }
            
            if (primo) {
                System.out.println(numero + " é primo!");
            } else {
                System.out.println(numero + " não é primo!");
            }
        }
        scanner.close();
    }
}