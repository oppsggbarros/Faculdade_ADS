import java.util.Scanner;

public class Exercicio16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o salário do trabalhador: R$ ");
        double salario = scanner.nextDouble();
        
        System.out.print("Digite o valor da prestação do empréstimo: R$ ");
        double prestacao = scanner.nextDouble();
        
        if (prestacao > (salario * 0.20)) {
            System.out.println("Empréstimo não concedido");
        } else {
            System.out.println("Empréstimo concedido");
        }
        
        scanner.close();
    }
}