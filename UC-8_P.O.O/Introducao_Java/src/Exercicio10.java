import java.util.Scanner;

public class Exercicio10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um número inteiro: ");
        int numero = scanner.nextInt();
        
        if (numero > 0) {
            int quadrado = numero * numero;
            double raiz = Math.sqrt(numero);
            
            System.out.println("Número ao quadrado: " + quadrado);
            System.out.printf("Raiz quadrada: %.2f\n", raiz);
        } else {
            System.out.println("O número não é positivo");
        }
        
        scanner.close();
    }
}