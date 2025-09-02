import java.util.Random;
import java.util.Scanner;

public class Exercicio39 {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);
        
        int numeroAleatorio = random.nextInt(100) + 1;
        int tentativas = 0;
        int palpite;
        
        System.out.println("Adivinhe o número entre 1 e 100!");
        
        do {
            System.out.print("Seu palpite: ");
            palpite = scanner.nextInt();
            tentativas++;
            
            if (palpite < numeroAleatorio) {
                System.out.println("Muito baixo!");
            } else if (palpite > numeroAleatorio) {
                System.out.println("Muito alto!");
            }
        } while (palpite != numeroAleatorio);
        
        System.out.println("Parabéns! Você acertou em " + tentativas + " tentativas.");
        scanner.close();
    }
}