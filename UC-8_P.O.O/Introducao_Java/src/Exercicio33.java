import java.util.Scanner;

public class Exercicio33 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o preço antigo do produto: R$ ");
        double precoAntigo = scanner.nextDouble();
        
        double aumento = 0;
        
        if (precoAntigo <= 50) {
            aumento = precoAntigo * 0.05;
        } else if (precoAntigo <= 100) {
            aumento = precoAntigo * 0.10;
        } else {
            aumento = precoAntigo * 0.15;
        }
        
        double precoNovo = precoAntigo + aumento;
        
        System.out.printf("Preço novo: R$ %.2f\n", precoNovo);
        
        if (precoNovo <= 80) {
            System.out.println("Barato");
        } else if (precoNovo <= 120) {
            System.out.println("Normal");
        } else if (precoNovo <= 200) {
            System.out.println("Caro");
        } else {
            System.out.println("Muito caro");
        }
        
        scanner.close();
    }
}