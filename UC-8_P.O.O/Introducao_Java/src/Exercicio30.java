import java.util.Scanner;

public class Exercicio30 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite a distância percorrida (Km): ");
        double distancia = scanner.nextDouble();
        
        System.out.print("Digite a quantidade de litros consumidos: ");
        double litros = scanner.nextDouble();
        
        if (litros <= 0) {
            System.out.println("Quantidade de litros inválida");
        } else {
            double consumo = distancia / litros;
            System.out.printf("Consumo: %.2f Km/l\n", consumo);
            
            if (consumo < 8) {
                System.out.println("Venda o carro!");
            } else if (consumo >= 8 && consumo <= 14) {
                System.out.println("Econômico!");
            } else {
                System.out.println("Super econômico!");
            }
        }
        
        scanner.close();
    }
}