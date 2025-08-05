import java.util.Scanner;

public class Exercicio15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o número de horas trabalhadas: ");
        double horas = scanner.nextDouble();
        
        double salarioBruto = horas * 40.50;
        double salarioLiquido;
        
        if (salarioBruto > 2500.00) {
            double imposto = (salarioBruto - 2500.00) * 0.11;
            salarioLiquido = salarioBruto - imposto;
        } else {
            salarioLiquido = salarioBruto;
        }
        
        System.out.printf("Salário líquido: R$ %.2f\n", salarioLiquido);
        
        scanner.close();
    }
}