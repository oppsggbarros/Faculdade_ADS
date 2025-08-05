import java.util.Scanner;

public class Exercicio8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um número: ");
        double numero = scanner.nextDouble();
        
        if (numero >= 0) {
            double raiz = Math.sqrt(numero);
            System.out.printf("A raiz quadrada de %.2f é %.2f\n", numero, raiz);
        } else {
            System.out.println("Número inválido");
        }
        
        scanner.close();
    }
}