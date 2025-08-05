import java.util.Scanner;

public class Exercicio29 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o valor do produto: R$ ");
        double valor = scanner.nextDouble();
        
        System.out.print("Digite o estado destino (MG, SP, RJ ou MS): ");
        String estado = scanner.next().toUpperCase();
        
        double imposto = 0;
        boolean estadoValido = true;
        
        switch (estado) {
            case "MG":
                imposto = valor * 0.07;
                break;
            case "SP":
                imposto = valor * 0.12;
                break;
            case "RJ":
                imposto = valor * 0.15;
                break;
            case "MS":
                imposto = valor * 0.08;
                break;
            default:
                System.out.println("Estado inválido");
                estadoValido = false;
        }
        
        if (estadoValido) {
            double valorFinal = valor + imposto;
            System.out.printf("Valor final do produto: R$ %.2f\n", valorFinal);
        }
        
        scanner.close();
    }
}