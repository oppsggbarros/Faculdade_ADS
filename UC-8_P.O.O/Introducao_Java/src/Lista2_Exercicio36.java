import java.util.Scanner;

public class Exercicio36 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o valor inicial e final do intervalo: ");
        int inicio = scanner.nextInt();
        int fim = scanner.nextInt();
        
        if (inicio > fim) {
            System.out.println("Intervalo de valores inválido");
        } else {
            int soma = 0;
            for (int i = inicio; i <= fim; i++) {
                if (i % 2 != 0) {
                    soma += i;
                }
            }
            System.out.println("Soma dos ímpares neste intervalo: " + soma);
        }
        scanner.close();
    }
}