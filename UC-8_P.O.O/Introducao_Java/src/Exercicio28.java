import java.util.Scanner;

public class Exercicio28 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite a idade do trabalhador: ");
        int idade = scanner.nextInt();
        
        System.out.print("Digite o tempo de serviço (em anos): ");
        int tempoServico = scanner.nextInt();
        
        boolean podeAposentar = false;
        
        if (idade >= 65) {
            podeAposentar = true;
        } else if (tempoServico >= 30) {
            podeAposentar = true;
        } else if (idade >= 60 && tempoServico >= 25) {
            podeAposentar = true;
        }
        
        if (podeAposentar) {
            System.out.println("Pode se aposentar");
        } else {
            System.out.println("Não pode se aposentar");
        }
        
        scanner.close();
    }
}