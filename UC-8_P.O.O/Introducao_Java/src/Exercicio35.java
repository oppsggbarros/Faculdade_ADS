import java.util.Scanner;

public class Exercicio35 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o salário atual do funcionário: R$ ");
        double salario = scanner.nextDouble();
        
        System.out.print("Digite o tempo de serviço (em anos): ");
        int tempo = scanner.nextInt();
        
        double reajuste = 0;
        double bonus = 0;
        
        if (salario <= 500) {
            reajuste = salario * 0.25;
        } else if (salario <= 1000) {
            reajuste = salario * 0.20;
        } else if (salario <= 1500) {
            reajuste = salario * 0.15;
        } else if (salario <= 2000) {
            reajuste = salario * 0.10;
        }
        
        if (tempo >= 1 && tempo <= 3) {
            bonus = 100;
        } else if (tempo >= 4 && tempo <= 6) {
            bonus = 200;
        } else if (tempo >= 7 && tempo <= 10) {
            bonus = 300;
        } else if (tempo > 10) {
            bonus = 500;
        }
        
        double salarioFinal = salario + reajuste + bonus;
        
        if (reajuste == 0 && bonus == 0) {
            System.out.println("Funcionário não tem direito a aumento");
        } else {
            System.out.printf("Salário final reajustado: R$ %.2f\n", salarioFinal);
        }
        
        scanner.close();
    }
}