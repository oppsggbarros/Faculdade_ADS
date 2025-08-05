import java.util.Scanner;

public class Exercicio36 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o custo de fábrica do carro: R$ ");
        double custoFabrica = scanner.nextDouble();
        
        double comissaoDistribuidor;
        double impostos;
        
        if (custoFabrica <= 12000) {
            comissaoDistribuidor = custoFabrica * 0.05;
            impostos = 0;
        } else if (custoFabrica <= 25000) {
            comissaoDistribuidor = custoFabrica * 0.10;
            impostos = custoFabrica * 0.15;
        } else {
            comissaoDistribuidor = custoFabrica * 0.15;
            impostos = custoFabrica * 0.20;
        }
        
        double custoConsumidor = custoFabrica + comissaoDistribuidor + impostos;
        
        System.out.printf("Custo ao consumidor: R$ %.2f\n", custoConsumidor);
        
        scanner.close();
    }
}