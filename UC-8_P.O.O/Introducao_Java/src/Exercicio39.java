import java.util.Scanner;

public class Exercicio39 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o tamanho da área a ser pintada (m²): ");
        double area = scanner.nextDouble();
        
        double litrosNecessarios = area / 6;
        
        // Opção 1: Apenas latas de 18 litros
        int latas18 = (int) Math.ceil(litrosNecessarios / 18);
        double precoLatas = latas18 * 80;
        
        // Opção 2: Apenas galões de 3.6 litros
        int galoes36 = (int) Math.ceil(litrosNecessarios / 3.6);
        double precoGaloes = galoes36 * 25;
        
        System.out.println("\nOpção 1: Comprar apenas latas de 18 litros");
        System.out.println("Quantidade de latas: " + latas18);
        System.out.printf("Preço total: R$ %.2f\n", precoLatas);
        
        System.out.println("\nOpção 2: Comprar apenas galões de 3.6 litros");
        System.out.println("Quantidade de galões: " + galoes36);
        System.out.printf("Preço total: R$ %.2f\n", precoGaloes);
        
        scanner.close();
    }
}