import java.util.Scanner;

public class Exercicio30 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] vetor = new int[10];
        
        // Preenche o vetor
        for (int i = 0; i < 10; i++) {
            vetor[i] = i * 2; // Exemplo: preenche com números pares
        }
        
        System.out.print("Digite um valor para verificar: ");
        int valor = scanner.nextInt();
        
        boolean encontrado = false;
        for (int i = 0; i < 10; i++) {
            if (vetor[i] == valor) {
                encontrado = true;
                break;
            }
        }
        
        if (encontrado) {
            System.out.println("Valor encontrado no vetor!");
        } else {
            System.out.println("Valor não encontrado no vetor.");
        }
        scanner.close();
    }
}