import java.util.Scanner;

public class Exercicio7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o valor de aquisição do produto: R$ ");
        double valorAquisicao = scanner.nextDouble();
        
        double valorVenda;
        
        if (valorAquisicao < 50.00) {
            valorVenda = valorAquisicao * 1.45;
        } else {
            valorVenda = valorAquisicao * 1.30;
        }
        
        System.out.printf("O valor de venda do produto é: R$ %.2f\n", valorVenda);
        
        scanner.close();
    }
}