import java.util.Scanner;

public class Exercicio18 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um número inteiro maior que zero: ");
        int numero = scanner.nextInt();
        
        if (numero <= 0) {
            System.out.println("Número inválido");
        } else {
            int soma = 0;
            int temp = numero;
            
            while (temp > 0) {
                soma += temp % 10;
                temp /= 10;
            }
            
            System.out.println("A soma dos algarismos é: " + soma);
        }
        
        scanner.close();
    }
}