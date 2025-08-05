import java.util.Scanner;

public class Exercicio40 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite quanto você ganha por hora: R$ ");
        double valorHora = scanner.nextDouble();
        
        System.out.print("Digite o número de horas trabalhadas no mês: ");
        double horasTrabalhadas = scanner.nextDouble();
        
        double salarioBruto = valorHora * horasTrabalhadas;
        double impostoRenda = salarioBruto * 0.11;
        double inss = salarioBruto * 0.08;
        double sindicato = salarioBruto * 0.05;
        double salarioLiquido = salarioBruto - impostoRenda - inss - sindicato;
        
        System.out.printf("\nSalário Bruto: R$ %.2f\n", salarioBruto);
        System.out.printf("Desconto IR (11%%): R$ %.2f\n", impostoRenda);
        System.out.printf("Desconto INSS (8%%): R$ %.2f\n", inss);
        System.out.printf("Desconto Sindicato (5%%): R$ %.2f\n", sindicato);
        System.out.printf("Salário Líquido: R$ %.2f\n", salarioLiquido);
        
        scanner.close();
    }
}