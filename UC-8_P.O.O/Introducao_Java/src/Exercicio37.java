import java.util.Scanner;

public class Exercicio37 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o peso (kg): ");
        double peso = scanner.nextDouble();
        
        System.out.print("Digite a altura (m): ");
        double altura = scanner.nextDouble();
        
        double imc = peso / (altura * altura);
        
        System.out.printf("IMC: %.2f - ", imc);
        
        if (imc < 18.5) {
            System.out.println("Abaixo do peso");
        } else if (imc <= 24.9) {
            System.out.println("Saudável");
        } else if (imc <= 29.9) {
            System.out.println("Peso em excesso");
        } else if (imc <= 34.9) {
            System.out.println("Obesidade Grau I");
        } else if (imc <= 39.9) {
            System.out.println("Obesidade Grau II (severa)");
        } else {
            System.out.println("Obesidade Grau III (mórbida)");
        }
        
        scanner.close();
    }
}