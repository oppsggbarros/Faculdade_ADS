import java.util.Scanner;

public class Exercicio25 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um ano: ");
        int ano = scanner.nextInt();
        
        boolean bissexto = false;
        
        if (ano % 400 == 0) {
            bissexto = true;
        } else if (ano % 100 == 0) {
            bissexto = false;
        } else if (ano % 4 == 0) {
            bissexto = true;
        }
        
        if (bissexto) {
            System.out.println(ano + " é um ano bissexto");
        } else {
            System.out.println(ano + " não é um ano bissexto");
        }
        
        scanner.close();
    }
}