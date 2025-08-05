import java.util.Scanner;

public class Exercicio32 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Cardápio:");
        System.out.println("100 - Hot Dog - R$ 12.00");
        System.out.println("102 - X-Salada - R$ 18.50");
        System.out.println("103 - X-Bacon - R$ 25.50");
        System.out.println("104 - X-Burguer - R$ 17.00");
        System.out.println("105 - Suco de Laranja - R$ 9.50");
        System.out.println("106 - Refrigerante - R$ 6.00");
        
        System.out.print("Digite o código do produto: ");
        int codigo = scanner.nextInt();
        
        System.out.print("Digite a quantidade: ");
        int quantidade = scanner.nextInt();
        
        double precoUnitario = 0;
        boolean codigoValido = true;
        
        switch (codigo) {
            case 100:
                precoUnitario = 12.00;
                break;
            case 102:
                precoUnitario = 18.50;
                break;
            case 103:
                precoUnitario = 25.50;
                break;
            case 104:
                precoUnitario = 17.00;
                break;
            case 105:
                precoUnitario = 9.50;
                break;
            case 106:
                precoUnitario = 6.00;
                break;
            default:
                System.out.println("Código inválido");
                codigoValido = false;
        }
        
        if (codigoValido) {
            double total = precoUnitario * quantidade;
            System.out.printf("Total a pagar: R$ %.2f\n", total);
        }
        
        scanner.close();
    }
}